def int_convert(f_in):
    def f_out(*args):
        args = [int(item) for item in args]
        return f_in(*args)
    return f_out

@int_convert
def somme(x, y):
    return x+y

@int_convert
def produit(x , y):
    return x*y

if __name__ == '__main__':
    print(somme(3.5 , 4.7)) # -> 7
    print(produit(3.5 , 4.7)) # -> 12