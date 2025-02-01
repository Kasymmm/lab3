#Define a functino histogram() that takes a list of integers and prints a histogram to the screen.

num=list(map(int, input().split()))
def histogram():
    for x in num:
        print("*"*x)
histogram()