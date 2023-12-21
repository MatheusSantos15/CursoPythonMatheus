v = str(input('Digite algo: '))
print(f''' 
    É Alpha númerico? {v.isalnum()},
    É alpha? {v.isalpha()},
    É Minuscula? {v.islower()},
    É maiuscula? {v.isupper()},
    Está capitalizada? {v.istitle()},
    É Decimal? {v.isdecimal()},
    É numérica? {v.isnumeric()},
    É espaço? {v.isspace()},
    Tipo: {type(v)}
      ''')
