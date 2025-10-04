##str1=input("Please enter the sentence:  ")
'''l=str.split()
max1=l[0]
min1=l[0]
for i in range(len(l)):
    if len(max1)<=len(l[i]):
        max1=l[i]
    elif len(min1)>=len(l[i]):
        min1=l[i]
print('Longest Word : ',max1)
print('Shortest word: ', min1)
str1=input("Please enter the sentence:  ")
str=str1.split()
dict={}
for i in range(len(str)):
    cnt = 0
    for j in str:
        if str[i]==j:
            cnt=cnt+1
    dict.update({str[i]:cnt})
print(dict)'''
import string
sentence=input("Plese enter the sentense:  ").lower()
sentence = sentence.translate(str.maketrans("", "", string.punctuation))
words=sentence.split()
#words1 = [word.replace(",", "") for word in words]
print(words)
word_count={}
for i in words:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]= 1
print(word_count)
'''
sentence = input("Please enter the sentence: ")
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)'''