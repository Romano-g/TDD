"""
1 - Receber um numero int
2 - Saber se o número é multiplo de 3 e 5:
    Bacon com ovos
3 - Saber se o número não é multiplo de 3 nem 5:
    Passa fome
4 - Saber se o número é multiplo somente de 3:
    Bacon
5 - Saber se o número é multiplo somente de 5:
    Ovos
"""


def bacon_with_eggs(x):
    assert isinstance(x, int), 'n deve ser Int'

    if x % 3 == 0 and x % 5 == 0:
        return 'Bacon with eggs'

    if x % 3 == 0 and x % 5 != 0:
        return 'Bacon'

    if x % 3 != 0 and x % 5 == 0:
        return 'Eggs'

    return 'Starve'
