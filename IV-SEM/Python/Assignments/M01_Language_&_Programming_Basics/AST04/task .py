def Reverse_String(s: str) -> str:
   reverse_string = ""  
   for char in s:
       reverse_string = char + reverse_string 
   return reverse_string        

if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
