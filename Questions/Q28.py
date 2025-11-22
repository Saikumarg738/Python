def largestnum(num):
    large=second=float('-inf')
    for i in num:
        if(i>large):
            second=large
            large=i
        elif(second<i<large):
            second=i
    return second

print(largestnum([5,2,6,4,8,9,7]))