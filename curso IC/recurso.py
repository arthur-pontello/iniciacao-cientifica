lista = [1,3,5,7,9]

def somarLista(lista, i):
    if i < 0:
        return 0
    return lista[i] + somarLista(lista, i - 1)

def horasEmMinutos(horas):
    return horas * 60

def minutosEmSegundos(minutos):
    return minutos * 60

def horasEmSegundos(horas):
    return horas * 3600

print(somarLista(lista, len(lista)-1))
print('Número de segundos:', horasEmSegundos(0.5), ' - Teste está correto?', horasEmSegundos(0.5)==1800.0)
print('Número de segundos:', horasEmSegundos(1.0), ' - Teste está correto?', horasEmSegundos(1.0)==3600.0)
print('Número de segundos:', horasEmSegundos(2.5), ' - Teste está correto?', horasEmSegundos(2.5)==9000.0)

def somarValores(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

print('Resultado:', somarValores(2), ' - Teste está correto?', somarValores(2)==2)
print('Resultado:', somarValores(2,4), ' - Teste está correto?', somarValores(2,4)==6)
print('Resultado:', somarValores(2,4,6), ' - Teste está correto?', somarValores(2,4,6)==12)
print('Resultado:', somarValores(1,2,3,4), ' - Teste está correto?', somarValores(1,2,3,4)==10)
print('Resultado:', somarValores(1,2,3,4,5), ' - Teste está correto?', somarValores(1,2,3,4,5)==15)

def retornarDia(dia):
    if dia < 1 or dia > 7:
        return None
    match dia:
        case 1:
            return 'domingo'
        case 2:
            return 'segunda'
        case 3:
            return 'terca'
        case 4:
            return 'quarta'
        case 5:
            return 'quinta'
        case 6:
            return 'sexta'
        case 7:
            return 'sabado'

print('Dia:', retornarDia(0), ' \t\t- resultado correto?', retornarDia(0)==None)
print('Dia:', retornarDia(1), ' \t\t- resultado correto?', retornarDia(1)=='domingo')
print('Dia:', retornarDia(2), ' \t- resultado correto?', retornarDia(2)=='segunda')
print('Dia:', retornarDia(3), ' \t- resultado correto?', retornarDia(3)=='terca')
print('Dia:', retornarDia(4), ' \t- resultado correto?', retornarDia(4)=='quarta')
print('Dia:', retornarDia(5), ' \t- resultado correto?', retornarDia(5)=='quinta')
print('Dia:', retornarDia(6), ' \t- resultado correto?', retornarDia(6)=='sexta')
print('Dia:', retornarDia(7), ' \t\t- resultado correto?', retornarDia(7)=='sabado')

def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

print(fatorial(5))

def combinacao(m, n):
    return int(fatorial(m)/(fatorial(m-n) * fatorial(n)))

print(combinacao(5,3))

def retornaDoisValores(*param):
    return sum(param), 2*sum(param)

print(retornaDoisValores(2, 3, 4))