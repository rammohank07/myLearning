import React, { useState, useEffect } from 'react';
import { getAuth, signInAnonymously, onAuthStateChanged } from 'firebase/auth';
import { initializeApp } from 'firebase/app';

// The main App component for our AWR report analyzer bot
const App = () => {
  // State variables to manage the application UI and data
  const [awrReport, setAwrReport] = useState('');
  const [analysisResult, setAnalysisResult] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [userId, setUserId] = useState(null);

  // Constants for API configuration. The API key is an empty string and will be handled by the Canvas environment.
  const API_KEY = "";
  const API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=" + API_KEY;
  
  // Initialize Firebase and set up authentication
  useEffect(() => {
    // Check if Firebase configuration is available
    if (typeof __firebase_config !== 'undefined' && typeof __initial_auth_token !== 'undefined') {
        try {
          const firebaseConfig = JSON.parse(__firebase_config);
          const app = initializeApp(firebaseConfig);
          const auth = getAuth(app);

          // Listen for authentication state changes
          const unsubscribe = onAuthStateChanged(auth, async (user) => {
              if (user) {
                  setUserId(user.uid);
                  console.log("Firebase signed in with user ID:", user.uid);
              } else {
                  console.log("Firebase not signed in. Attempting anonymous sign-in.");
                  try {
                      // Sign in anonymously if not already authenticated
                      await signInAnonymously(auth);
                  } catch (signInError) {
                      console.error("Firebase Anonymous Sign-in Error:", signInError);
                  }
              }
          });

          // Cleanup the listener on component unmount
          return () => unsubscribe();
        } catch (initError) {
            console.error("Firebase initialization failed:", initError);
            setError("Failed to initialize Firebase. Please try again.");
        }
    } else {
        console.error("Firebase config or auth token is missing.");
    }
}, []);

  // Function to handle the analysis request
  const handleAnalyze = async () => {
    // Prevent analysis if the report text is empty or analysis is already in progress
    if (!awrReport.trim() || isLoading) return;

    // Reset state and show loading indicator
    setAnalysisResult('');
    setError(null);
    setIsLoading(true);

    try {
      // Create a specific, detailed prompt for the LLM to analyze the AWR report
      const prompt = `You are an expert Oracle DBA. Analyze the following AWR (Automatic Workload Repository) report.
    '''
      Your analysis should be structured as follows:
      1.  **Summary of Key Findings:** Provide a high-level overview of the databases performance during the reported period. Is it healthy, or are there significant issues?
      2.  **Top 5 Bottlenecks:** Based on the Top 5 Timed Foreground Events and other relevant sections, identify the primary performance bottlenecks. For each bottleneck, explain what it means and why it's a problem.
      3.  **Key Metrics and Observations:** Comment on the health of the database based on the following metrics:
          * **Load Profile:** Is the database busy (e.g., high DB Time)?
          * **Wait Class:** What are the major wait classes? (e.g., CPU, I/O, Concurrency)
          * **SQL Statistics:** Are there any top-consuming SQL statements (by Elapsed Time, CPU, or I/O) that stand out?
          * **I/O Profile:** Are there high I/O wait times or top I/O segments?
      4.  **Actionable Recommendations:** Provide specific, numbered recommendations to resolve the identified bottlenecks. The recommendations should be clear, concise, and prioritized from most to least impactful.
      '''
      AWR Report to Analyze:
      ---
      ${awrReport}
      ---
      `;

      // Construct the payload for the API call
      const payload = {
        contents: [{ role: "user", parts: [{ text: prompt }] }],
      };

      // Exponential backoff for API call retry
      let response;
      let retries = 0;
      const maxRetries = 5;
      while (retries < maxRetries) {
        try {
          response = await fetch(API_URL, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
          });

          if (response.status === 429) { // Too Many Requests
            retries++;
            const delay = Math.pow(2, retries) * 1000;
            await new Promise(res => setTimeout(res, delay));
            continue;
          }

          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }

          break; // Success, exit the loop
        } catch (fetchError) {
          if (retries === maxRetries - 1) {
            throw fetchError;
          }
          retries++;
          const delay = Math.pow(2, retries) * 1000;
          await new Promise(res => setTimeout(res, delay));
        }
      }

      // Parse the JSON response
      const result = await response.json();

      // Check for valid response structure and extract the text
      if (result.candidates && result.candidates.length > 0 &&
          result.candidates[0].content && result.candidates[0].content.parts &&
          result.candidates[0].content.parts.length > 0) {
        const text = result.candidates[0].content.parts[0].text;
        setAnalysisResult(text);
      } else {
        setError('Could not get a valid analysis from the model. Please check the report format.');
        console.error('API response was not in the expected format:', result);
      }

    } catch (apiError) {
      // Handle any errors during the API call
      console.error('Error during API call:', apiError);
      setError('An error occurred during analysis. Please try again later.');
    } finally {
      // Hide the loading indicator
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center p-8 bg-gray-100 min-h-screen font-sans">
      <div className="w-full max-w-4xl p-8 bg-white rounded-2xl shadow-xl">
        {/* Title of the application */}
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-6">AWR Report Analyzer Bot</h1>
        
        {/* User ID display for collaborative purposes */}
        <div className="text-sm text-gray-500 mb-4 text-center">
          User ID: <span className="font-mono text-xs">{userId || 'Authenticating...'}</span>
        </div>

        {/* Text area for user to paste the AWR report */}
        <textarea
          className="w-full h-80 p-4 border-2 border-gray-300 rounded-xl mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 resize-none"
          placeholder="Paste your AWR (Automatic Workload Repository) report here..."
          value={awrReport}
          onChange={(e) => setAwrReport(e.target.value)}
          disabled={isLoading}
        ></textarea>

        {/* Button to trigger the analysis */}
        <button
          className={`w-full px-6 py-3 rounded-xl font-semibold transition-all duration-300 ${
            isLoading
              ? 'bg-blue-300 cursor-not-allowed'
              : 'bg-blue-600 text-white hover:bg-blue-700 shadow-md'
          }`}
          onClick={handleAnalyze}
          disabled={isLoading}
        >
          {isLoading ? 'Analyzing...' : 'Analyze Report'}
        </button>

        {/* Display area for analysis results */}
        {isLoading && (
          <div className="mt-4 text-center text-blue-600 font-medium">
            Thinking... Your analysis is being generated.
          </div>
        )}

        {error && (
          <div className="mt-4 text-center text-red-600 font-medium p-4 bg-red-100 rounded-lg">
            {error}
          </div>
        )}

        {analysisResult && (
          <div className="mt-6 p-6 bg-gray-50 border-2 border-gray-200 rounded-xl whitespace-pre-wrap leading-relaxed shadow-inner">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">Analysis Result</h2>
            {/* The result is displayed here, preserving newlines from the models output */}
            {analysisResult}
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
