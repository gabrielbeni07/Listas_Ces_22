def is_palindrome(s):
   """Function that recognizes palindromes"""
   
   w = ""
   for i in s:
       w = i + w
   
   if(s == w):
       print("Yes")
   else:
       print("No")
