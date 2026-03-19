
# Questão 1

print(""""

        ***********
       *           *
      *             *
      *             *
       *           *
        ***********
      
                 *
                  *
     ************** **
                  *
                *
      
          *
        *   *
      *       *
    *           *
      *       *
        *   *
          *
""")

# Questao 2
print()
x = input("Entre com um número: ")
base = input("Escolha uma base (8, 10, 16): ")

x = int(x)

if base == "8": 
    print(f"Octal: {oct(x)}")
elif base == "10":
    print(f"Decimal: {x}")
elif base == "16":
    print(f"Hexa: {hex(x)} ")
else:
    print("Base inválida")

# Questao 3
print(f"Igual a {3 + 4 - 0 * 1 / 1 // 1 % 1 ** 1}")
print(f"Igual a {10 + 3 - 0 * 1 / 1 // 1 % 1 ** 1}")
print(f"Igual a: {7//2 + 0.5 - 0 * 1 / 1 // 1 % 1 ** 1}")

# Questao 4
print()
frase = "Anotaram a data da maratona"

print(len(frase))
print(f"{frase[0]}, {(frase[-1])}")
print(frase[::-1])

#Questao 5
print()
dataMensagem = "2026-03-12 09:15:07 - login ok"

print(dataMensagem[0:10])
print(dataMensagem[11:20])
print(dataMensagem[22:])

#Questao 6
print()
texto = input("Entre com a mensagem: ")
deslocamento = int(input("Deslocamento: "))

texto_cifrado = ""

for letra in texto:
    if letra.isalpha():
        base = ord('A') if letra.isupper() else ord('a')
        letra_cifrada = chr((ord(letra) - base + deslocamento) % 26 + base)
        texto_cifrado += letra_cifrada
    else:
        texto_cifrado += letra 

print("Texto cifrado:", texto_cifrado)

# Questao 7
print()
frase = input("Digite uma frase: ")

vogais = "aeiou"
contagem = 0

for letra in frase.lower():
    if letra in vogais:
        contagem += 1

print(f"Quantidade de vogais: {contagem}")

# Questao 8
