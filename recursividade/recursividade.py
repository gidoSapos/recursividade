def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
fatorial(4)

def soma_recursiva(n):
    if n == 0:
        return 1
    else:
        return n + fatorial(n - 1)
soma_recursiva(5)

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return n + fatorial(n)
fibonacci(4)

def palindromo(palavra):
    if len(palavra) <= 1:
        return True
    elif palavra[0] != palavra[-1]:
        return False
    else:
        return palindromo(palavra[1:-1])
    
palindromo('sacole')

def inverter_string(s):
    if len(s) == 0:
        return s
    else:
        return inverter_string(s[1:]) + s[0]    
inverter_string('elocas')

def contar_digitos(n):
    if n == 0:
        return 0
    else:
        return 1 + contar_digitos(n // 10)
contar_digitos(23843874)

def maior_elemento(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        maior_restante = maior_elemento(vetor[1:])
        return vetor[0] if vetor[0] > maior_restante else maior_restante
maior_elemento([2,3,123,12,3,12,3,54,6])

def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)
potencia(5,6)


def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f'Move disco 1 da torre {origem} pra a torre {destino}')
    else:
        torres_de_hanoi(n - 1, origem, auxiliar, destino)
        print(f'Mover o disco {n} da torre {origem} para a torre {destino}')
        torres_de_hanoi(n - 1, auxiliar, destino, origem)

torres_de_hanoi(1, 'A', 'C', 'B')