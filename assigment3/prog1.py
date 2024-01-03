def isPalindrome(string):

 if (string== string[::-1]):
  print("The string is a palindrome.")
 else:
  print("The string is not a palindrome.")


string=input("Enter string:")

print(isPalindrome(string))