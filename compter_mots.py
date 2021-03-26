
def compteMots(chaine):
    list = dict([(chaine[i], chaine.count(chaine[i])) for i in range(len(chaine))])
    list = dict([(cara, chaine.count(cara)) for cara in set(chaine)])
    return list

list=compteMots("aaa bbcce")
print(list)