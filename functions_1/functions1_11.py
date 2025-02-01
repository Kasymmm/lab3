#Write a Python function that checks whether a word or phrase is palindrome or not. 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

s=str(input())

def func(s):
    for x in range(len(s)//2):
        if s[x]!=s[len(s)-x-1]:
            return False
    return True
print(func(s))