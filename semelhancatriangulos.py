def lados_proporcionais(lado1_t1, lado2_t1, lado1_t2, lado2_t2):
    return abs((lado1_t1 / lado1_t2) - (lado2_t1 / lado2_t2)) < 0.001

def semelhança_LAL(lado1_t1, lado2_t1, angulo_t1, lado1_t2, lado2_t2, angulo_t2):
    if angulo_t1 == angulo_t2 and lados_proporcionais(lado1_t1, lado2_t1, lado1_t2, lado2_t2):
        return True
    return False

def semelhança_AA(angulo1_t1, angulo2_t1, angulo1_t2, angulo2_t2):
    if angulo1_t1 == angulo1_t2 and angulo2_t1 == angulo2_t2:
        return True
    return False

def semelhança_LLL(lado1_t1, lado2_t1, lado3_t1, lado1_t2, lado2_t2, lado3_t2):
    if lados_proporcionais(lado1_t1, lado2_t1, lado1_t2, lado2_t2) and lados_proporcionais(lado2_t1, lado3_t1, lado2_t2, lado3_t2):
        return True
    return False

def verificar_semelhança():
    print("Escolha o critério de semelhança: LAL, AA ou LLL")
    criterio = input().upper()

    if criterio == 'LAL':
        lado1_t1 = float(input("Digite o primeiro lado do triângulo 1: "))
        lado2_t1 = float(input("Digite o segundo lado do triângulo 1: "))
        angulo_t1 = float(input("Digite o ângulo entre eles do triângulo 1: "))
        lado1_t2 = float(input("Digite o primeiro lado do triângulo 2: "))
        lado2_t2 = float(input("Digite o segundo lado do triângulo 2: "))
        angulo_t2 = float(input("Digite o ângulo entre eles do triângulo 2: "))
        if semelhança_LAL(lado1_t1, lado2_t1, angulo_t1, lado1_t2, lado2_t2, angulo_t2):
            print("Os triângulos são semelhantes pelo critério LAL.")
        else:
            print("Os triângulos não são semelhantes pelo critério LAL.")
    
    elif criterio == 'AA':
        angulo1_t1 = float(input("Digite o primeiro ângulo do triângulo 1: "))
        angulo2_t1 = float(input("Digite o segundo ângulo do triângulo 1: "))
        angulo1_t2 = float(input("Digite o primeiro ângulo do triângulo 2: "))
        angulo2_t2 = float(input("Digite o segundo ângulo do triângulo 2: "))
        if semelhança_AA(angulo1_t1, angulo2_t1, angulo1_t2, angulo2_t2):
            print("Os triângulos são semelhantes pelo critério AA.")
        else:
            print("Os triângulos não são semelhantes pelo critério AA.")
    
    elif criterio == 'LLL':
        lado1_t1 = float(input("Digite o primeiro lado do triângulo 1: "))
        lado2_t1 = float(input("Digite o segundo lado do triângulo 1: "))
        lado3_t1 = float(input("Digite o terceiro lado do triângulo 1: "))
        lado1_t2 = float(input("Digite o primeiro lado do triângulo 2: "))
        lado2_t2 = float(input("Digite o segundo lado do triângulo 2: "))
        lado3_t2 = float(input("Digite o terceiro lado do triângulo 2: "))
        if semelhança_LLL(lado1_t1, lado2_t1, lado3_t1, lado1_t2, lado2_t2, lado3_t2):
            print("Os triângulos são semelhantes pelo critério LLL.")
        else:
            print("Os triângulos não são semelhantes pelo critério LLL.")
    else:
        print("Critério inválido! Escolha entre LAL, AA ou LLL.")

verificar_semelhança()
