'''n = int(input())
count = 0    
while n > 0 :
    count =+ 1 
    n = n // 10 
print(count) 
'''
'''n = int(input())  
while n >0:
    digit = n % 10
    if digit % 2 == 0 :
        print(digit , end = " ") 
    n = n // 10    '''  

'''n = int(input())
sum = 0 
while n > 0 :
    digit = n % 10 
    if digit ==  n * 10 : 
         sum = + n 
         print(sum )
    n = n //10 '''  
'''def reverse(num):
    rev = 0 
    while num > 0:
        rev = (rev *10) + (num % 10) 
        num = num // 10 
    return rev 
n = int(input()) 
while n > 0:
    digit = n % 10 
    if digit % 2 == 0:
         print(digit, end=" ") 
    n = n //10     '''  
n = int(input())  
temp = reverse(n) 
if temp == n: 
    print("yes") 
else: 
    print("no")           