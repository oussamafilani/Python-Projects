def fonPalindrome(chaine) :
    return chaine == chaine[::-1]

    # for i in (len(chaine)):
    #     palindrome = True
    #     if chaine[i] != chaine[-(i+1)]:
    #         palindrome =False
    #         break
    # return palindrome


chaine = "ressasser"
str = fonPalindrome(chaine)
 
if str:
    print("Yes")
else:
    print("No")

# print(fonPalindrome("ressasser"))
