num=list(map(int, input().split()))
print(num)

def has_33(num):
    for x in range(len(num)-1):
        if num[x]==num[x+1]==3:
            return True
    return False
x=has_33(num)
print(x)