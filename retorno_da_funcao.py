def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
   # print("Ola mundo!")
    return # se não tiver com valr explicito retornara NONE

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10)) #retorna uma tupla, é imutavel
print(func_3()) #none