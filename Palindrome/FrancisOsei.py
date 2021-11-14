
# string palindrome

def stringPalindrome(string):
    """check whether string is palindrome or not"""
    if string == string[::-1]:
        return f'{string} is a palindrome'
    return f'{string}is not a palindrome'


print(stringPalindrome('madam'))
