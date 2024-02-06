def check_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")
try:
    file = input("Enter filepath for palindrome check: ")
    text = open(file, "r").read()
    check_palindrome(text)
except:
     print(f"Unable to process file at {path}")
     