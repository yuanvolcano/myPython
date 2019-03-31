def reverse(text):
  print(text[::-1])
  return text[::-1]

def is_palindrome(text):
  return text == reverse(text)

something = input("Enter text:")
if is_palindrome(something):
  print('Yes, it is a palindrome')
else:
  print("no, it is not a palindrome")
