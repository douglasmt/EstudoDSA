# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação desejada:\n")

print("\n1 - Soma")
print("\n2 - Substração")
print("\n3 - Multiplicação")
print("\n4 - Divisão\n")
opcao = int(input(print("\nDigite a opção: ")))

n1 = float(input(print("\nDigite o primeiro número: ")))
n2 = float(input(print("\nDigite o segundo número: ")))

if opcao == 1:
    soma = n1 + n2    
    print("Soma " + str(int(n1)) + " + " + str(int(n2)) 
          + " é igual a " + str(int(soma)))
elif opcao == 2:
    subtr = n1 - n2    
    print("Subtração " + str(int(n1)) + " - " + str(int(n2)) 
          + " é igual a " + str(int(subtr)))
elif opcao == 3:
    mult = n1 * n2    
    print("Multiplicação " + str(int(n1)) + " X " + str(int(n2)) 
          + " é igual a " + str(int(mult)))
elif opcao == 4:
    divisao = n1 / n2    
    print("Divisão " + str(int(n1)) + " / " + str(int(n2)) 
          + " é igual a " + str(int(divisao)))
else:
  print("Opção inválida")

      
