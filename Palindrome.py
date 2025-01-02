def ispalindrome(string):
 left_pos = 0
 right_pos = len(string)- 1
 if not(string[left_pos]==string[right_pos]): 
  print("False")
 else:
  print("True")
print("Is this a palindrome?")
print(ispalindrome("malayalam")) 