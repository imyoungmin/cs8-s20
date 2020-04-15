'''
Given a string *s* of length 5, write a function to determine if *s* is palindromic.

'''

def isPalindromic(s):
    for i in range (0, 2):
        if s[i] != s[4-i]:
            return False
    return True

def main():
    s = input()
    print(isPalindromic(s))

if __name__ == '__main__':
    main()