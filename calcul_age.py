from datetime import date

def caculeAge(naissance) :

    ajourdhui = date.today()
    anniversaire = naissance.replace(year=ajourdhui.year)
    if anniversaire < ajourdhui :
        return ajourdhui.year - naissance.year
    else:
        return ajourdhui.year - naissance.year -1


age = caculeAge(date(1988,3,28))
print("Your age is :",age)