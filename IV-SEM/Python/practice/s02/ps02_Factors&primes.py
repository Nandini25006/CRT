'''
Factors 
12 => 1,2,3,4,6,12 
'''  
'''  
print all factors of the give number  
'''  
'''n = int(input()) 
for i in range(1, n+1): 
    if n % i == 0:
        print(i) 
        ''' 
'''n = int(input())  
for i in range(1, n//2+1):
    if n % i == 0: 
        print(i) 
print(n)     '''  
'''n = int(input()) 
for i in range(1, n//2+1):
    count = 0 
    if n % i == 0 :
        count =+i
print(count) '''  
'''n = int(input()) 
count = 0 
for i in range(2 , n//2):
    if n % i ==0:
        count+=1 
if count == 0:
    print("prime")         
else:
    print("Not prime")  '''   
 '''
 prime all the prime number in the give range 
input: 1 10 
output : 2 5 7 
 
n = int(input()) 
m = int(input())
for n  in range(n, m): 
    count =0 
   for i in range(2, n//2+1):
      if n %i == 0:
         count += 1 
    if count == 0:
        print(n)     
Read a number from the user and display factorial of a number 
input: 5 
output: 120  

n = int(input()) 
fact = 1 
for i in range(1,n+1):
   fact = fact *i
print(fact)''' 

     
 
