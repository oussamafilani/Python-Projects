
def cap(chaine):
    if '.' not in chaine:
        return chaine.lstrip().capitalize().rjust(len(chaine))
    else:
        phrases = chaine.split(".")
        phrases = [cap(item) for item in phrases]
        return ".".join(phrases)


print(cap('    cecI est UNE chaine'))
print(cap(('             chaine. test. oussama . oussAma')))





