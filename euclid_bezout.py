DEBUG = False

def eh_par(n):
    if (n % 2) == 0:
        return True
    else:
        return False

def coeficientes(alfa, resto_lm, quociente, ab_rm):
    i = len(alfa) - 1
    y = (alfa[i]*ab_rm[0] - quociente[0])//resto_lm[0]
    x = (y * ab_rm[1] - 1)//-(ab_rm[0])
    return x, y

def metade_restos (resto_l, rn):
    resto_lm = [int(linha) // rn for linha in resto_l]
    return resto_lm

def calcula_alfa(n, resto_lm, quociente):
    alfa_i = [1]

    # define número de iterações
    i = n // 2 if eh_par(n) else (n - 1) // 2

    # define valores de k e l
    k, l = (2, 0) if eh_par(n) else (3, 1)

    linha = 1
    while (linha <= i):
        q = (alfa_i[linha - 1] * resto_lm[n - k] - quociente[n - l]) // resto_lm[n - l]
        alfa_i.append(q)
        k += 2
        l += 2
        linha+=1
    return alfa_i

def verifica (ab, a, x, y):
    c = ab[0] * x + ab[1] * y
    if (c==a):
        return True
    else:
        return False

def mdc_extendido(a, b):

    resto = 1
    ab = [a, b]
    resto_l = []
    quociente = []
    
    # verificação triviais
    if (a == 0 and b == 0): return 0, 0, 0
    if (b == 0 and a != 0): return a, 1, 0
    elif (a == 0 and b!= 0): return b, 0, 1
    elif(a == b): return a, 1, 0
    elif (a % b == 0): return b, 0, 1

    else:

        while (resto != 0):
            resto = a % b
            resto_l.append(resto)
            quociente.append(a//b)
            a, b = b, resto # atualização de valores

        resto_lm = metade_restos(resto_l, a)
        ab_lm = metade_restos(ab, a)
        pos_rn = resto_l.index(a)
        alfa = calcula_alfa(pos_rn, resto_lm, quociente)
        x, y = coeficientes(alfa, resto_lm, quociente, ab_lm)

        if (DEBUG):
            print ("\nTabela de restos: ", resto_l)
            print("Valores dos quocientes: ", quociente)
            print("Valor de rn: ", pos_rn)
            print("Após a divisão por rn: ", ab_lm, resto_lm)
            print("Valores de alfa_i: ", alfa)
            print(verifica(ab, a, x, y), "\n")
            
        return a, x, y

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
mdc, x, y = mdc_extendido(a, b)
print ("MDC :", mdc)
print("x: ", x)
print("y: ", y)
