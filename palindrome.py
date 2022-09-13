import sys

def pal():
    
    sentence = sys.argv[1]
    sent_list = sentence.lower().split()
    is_palindrome = lambda phrase: phrase == phrase[::-1]
    is_pal = is_palindrome(sent_list)
    if is_pal == True:
        print("It's a palindrome!")
    elif sent_list[0][0] == sent_list[-1][-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

pal()