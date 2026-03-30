'''#1.(find the largest number (using max))
#input:[12,78,32,54,69,100]
#output:100
li = list(map(int,input().split()))
max_num = li[0]
for element in li:
    if element > max_num:
        max_num = element
print(max_num)
print(max(li))
print(min(li))

s = input()
print("palindrome" if s == s[::-1] else "not palindrome")
print("".join(reversed(s)))'''

#count even number from the list

s = input()
for i in range(s):
    if i%2 == 0:
        print("Even")
    else:
        print("Odd")