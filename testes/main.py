from calculadora import my_sum


try:
    print(my_sum(10, 20))
except AssertionError as e:
    print(f'Conta inválida: {e}')
