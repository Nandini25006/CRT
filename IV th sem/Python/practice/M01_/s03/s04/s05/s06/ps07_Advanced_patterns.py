'''1. pascal Triangle 
n = 5 
output:
1
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 '''  
'''n = int(input()) 
for i in range(1 , n+1):
    c = 1 
    for j in range(i):
        c = (c * (i-j) // (j+1))
    print(c, end=" ")'''
'''2. butterfly pattern
n =4 
output:
*   * 
**  **
*** ***
********
********
*** ***
**  **
*   *
'''