#define a function
def ispalindrome(string):
                if string == string[::-1]:
                                 return"the string is a palindrome."
                else:
                                  return"the string is not a palindrome."
#Enter input string


string = input("Enter string:")
print(ispalindrome(string))
                
