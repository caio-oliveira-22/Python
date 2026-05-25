import soma
import subtrair
import multiplicar
import divisao
import potencia
import raizquadrada
import cambio


def calculadora():
    
    
    print("DECIDA QUAL NÚMERO")
    escolha = input("\n1 para soma, \n2 para subtrair, \n3 para multiplicar, \n4 para divisao, \n5 para potemcia, \n6 para tirar a raiz, \n7 para conversão de dinheiro: ")

    
    if escolha == "1":

        a = int(input("Digite A: "))
        b = int(input("Digite B: "))
        
        dados = soma.soma(a,b)
        print(dados)

    elif escolha == "2":

        a = int(input("Digite A: "))
        b = int(input("Digite B: "))

        dados = subtrair.subtrair(a,b)
        print(dados)

    elif escolha == "3":

        a = int(input("Digite A: "))
        b = int(input("Digite B: "))

        dados = multiplicar.multiplicar(a,b)
        print(dados)

    elif escolha == "4":

        a = int(input("Digite A: "))
        b = int(input("Digite B: "))

        dados = divisao.dividir(a,b)
        print(dados)
    elif escolha == "5":

        a = int(input("Digite A: "))
        b = int(input("Digite B: "))

        dados = potencia.potencia(a,b)
        print(dados)

    elif escolha == "6":

        a = int(input("Digite A: "))
        b = int(input("Digite B: "))
        
        dados = raizquadrada.raiz(a)
        print(dados)

    elif escolha == "7":
        valor_real = float(input("Digite o valor em reais: "))
        valor_dolar = valor_real / float(cambio.cotacao_dolar())
        print(valor_dolar)


        

