def fatorial (x):
    
    fator=1    
    while x > 1:
        fator = x*fator
        x=x-1
    return fator


def binomial (x,y):
    return fatorial(x)/(fatorial(y)*fatorial(x-y))

x=int(input("Digite o priemiro digito: "))
y=int(input("Digite o segundo digito: "))

print(binomial(x,y))
