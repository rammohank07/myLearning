import os
import json
import time
import requests

def analyze_awr_report_with_gemini(awr_report_text):
    """
    Analyzes an AWR report using the Gemini API and provides structured
    feedback and recommendations.

    Args:
        awr_report_text (str): The raw text of the AWR report.

    Returns:
        str: The analysis result from the AI model, or an error message.
    """
    # NOTE: In a real-world application, you would manage your API key securely
    # (e.g., using environment variables). For this example, you can
    # paste it directly here.
    # Replace 'YOUR_API_KEY' with your actual Gemini API key.
    api_key = os.environ.get("GEMINI_API_KEY", "") 

    # The API endpoint for the Gemini model
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"

    # The prompt is a critical part of the process. It acts as an instruction set
    # for the AI model, telling it how to act and what to focus on.
    # We instruct the model to act as an expert Oracle DBA and structure its response.
    prompt = f"""
    You are an expert Oracle DBA. Analyze the following AWR (Automatic Workload Repository) report.
    
    Your analysis should be structured as follows:
    1.  **Summary of Key Findings:** Provide a high-level overview of the database's performance during the reported period. Is it healthy, or are there significant issues?
    2.  **Top 5 Bottlenecks:** Based on the 'Top 5 Timed Foreground Events' and other relevant sections, identify the primary performance bottlenecks. For each bottleneck, explain what it means and why it's a problem.
    3.  **Key Metrics and Observations:** Comment on the health of the database based on the following metrics:
        * **Load Profile:** Is the database busy (e.g., high DB Time)?
        * **Wait Class:** What are the major wait classes? (e.g., CPU, I/O, Concurrency)
        * **SQL Statistics:** Are there any top-consuming SQL statements (by Elapsed Time, CPU, or I/O) that stand out?
        * **I/O Profile:** Are there high I/O wait times or top I/O segments?
    4.  **Actionable Recommendations:** Provide specific, numbered recommendations to resolve the identified bottlenecks. The recommendations should be clear, concise, and prioritized from most to least impactful.
    
    AWR Report to Analyze:
    ---
    {awr_report_text}
    ---
    """
    
    # The payload is the data sent to the API, including the prompt and chat history.
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    # Exponential backoff retry logic to handle rate limiting or temporary errors.
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            # Send the request to the Gemini API
            response = requests.post(api_url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            # Check for valid response and extract the text.
            result = response.json()
            if result.get("candidates") and len(result["candidates"]) > 0:
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return "Could not get a valid analysis from the model. Please check the report format."

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Too Many Requests
                retries += 1
                delay = 2**retries  # Exponential delay
                print(f"Rate limit hit. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                return f"An HTTP error occurred: {e}"
        except Exception as e:
            return f"An error occurred during analysis: {e}"

    return "Max retries exceeded. Please try again later."


# --- Example Usage ---

# 1. Paste your AWR report content here within the triple quotes.
#    This is a dummy report for demonstration purposes.
#    Replace this with your actual AWR report text.
dummy_awr_report = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Snap Id      Snap Time      Sessions Curs/Sess
    --------- ------------------- -------- ---------
      35002 01-Jun-24 10:00:00        243      3.2
      35003 01-Jun-24 11:00:00        245      3.4
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Top 5 Timed Foreground Events
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Event                          Waits    Time(s) Avg wait (ms) % DB time
    ------------------------------ -------- -------- ------------- ---------
    DB CPU                             -    2,500          -        60.0
    db file sequential read      1,000,000    1,500       1.5        30.0
    log file sync                  50,000       500      10.0        10.0
    ... rest of the report ...
"""

# 2. Call the analysis function with your AWR report text.
print("Starting AWR report analysis...")
analysis_output = analyze_awr_report_with_gemini(dummy_awr_report)

# 3. Print the results.
print("\n--- AWR Report Analysis ---")
print(analysis_output)
print("--------------------------")
