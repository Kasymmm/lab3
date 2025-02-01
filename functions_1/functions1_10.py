#Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Note: don't use collection set.

num=list(map(int, input().split()))
def func(num):
    uni=[]
    for x in num:
        if x not in uni:
            uni.append(x)
    return uni
new=func(num)
print(new)