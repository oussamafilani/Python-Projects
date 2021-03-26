def fonPalindrome(chaine) :

    for i in (len(chaine)):
        palindrome = True
        if chaine[i] != chaine[-(i+1)]:
            palindrome =False
            break
    return palindrome




print(fonPalindrome("ressasser"))
