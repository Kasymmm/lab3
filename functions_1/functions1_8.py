num=list(map(int, input().split()))


def zero(num):
    for x in range(len(num)-1):
        if num[x]==num[x+1]==0 and num[x+2]==7:
            return True
    return False
a=zero(num)   
print(a)