
# Questao 1

print()

x = input("Digite a frase: ")
limpa = ''.join(c.lower() for c in x if c.isalnum())
invertida = limpa[::-1]

if limpa == invertida:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")

# Questao 2

print()

hora = input("Digite a hora (formato HH): ")
chuva = input("Está chovendo? (0: não, 1: sim): ")
fluxo = input("O fluxo de carros está alto? (0: baixo, 1: médio, 2: alto): ")

hora = int(hora)

if hora < 0 or hora > 23:
    print("Hora inválida. Digite um valor entre 0 e 23.")
    exit()

chuva = bool(int(chuva))
fluxo = int(fluxo)

tempoSeg = 0

if (hora in range(7, 10)) or (hora in range(17, 20)):
    tempoSeg += 60
else:
    tempoSeg += 35

if chuva:
        tempoSeg *= 1.2

if fluxo == 2 :
    tempoSeg += 15
elif fluxo == 0 :
    tempoSeg -= 10

print(f"O semaforo está em: {tempoSeg:.2f} segundos")

#  Questao 3

print()

print()
palavraComparada = input("Digite uma palavra: ").lower()
palavraAnagrama = input("Digite outra palavra: ").lower()

contagem1 = {}
for letra in palavraComparada:
    contagem1[letra] = contagem1.get(letra, 0) + 1

contagem2 = {}
for letra in palavraAnagrama:
    contagem2[letra] = contagem2.get(letra, 0) + 1

if contagem1 == contagem2:
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")


# Questao 4

print()

palavras = ["banana", "abacaxi", "laranja", "uva", "melancia"]

palavraBuscada = input("Digite uma palavra: ").lower()

encontrada = False
for i, palavra in enumerate(palavras):
    if palavra == palavraBuscada:
        print(f"Índice: {i}, Palavra: {palavra}")
        encontrada = True
        break

if not encontrada:
    print("Palavra não encontrada.")


# Questao 5

print()

a = int(input("Digite a: "))
b = int(input("Digite b: "))
p = int(input("Digite p: "))

if p == 0:
    print("Erro: p não pode ser zero.")
elif a < b and p < 0:
    print("Erro: p deve ser positivo quando a < b.")
elif a > b and p > 0:
    print("Erro: p deve ser negativo quando a > b.")
elif a == b:
    print("Erro: a e b são iguais.")
else:
    count = 0
    for i in range(a, b + (1 if p > 0 else -1), p):
        print(i)
        count += 1
    print(f"Total de valores impressos: {count}")

# Questao 6

print()

estado = None

while True:
    cmd = input("Comando (A/T/E/F/S): ").upper()

    match cmd:
        case "A":
            if estado is None:
                estado = "aberto"
                print("Atendimento aberto.")
            else:
                print(f"Erro: atendimento já está '{estado}'.")

        case "T":
            if estado == "aberto":
                estado = "triado"
                print("Triagem realizada.")
            elif estado is None:
                print("Erro: nenhum atendimento aberto.")
            else:
                print(f"Erro: triagem inválida no estado '{estado}'.")

        case "E":
            if estado == "triado":
                estado = "encaminhado"
                print("Atendimento encaminhado.")
            elif estado is None:
                print("Erro: nenhum atendimento aberto.")
            else:
                print(f"Erro: encaminhamento inválido no estado '{estado}'.")

        case "F":
            if estado == "encaminhado":
                estado = "finalizado"
                print("Atendimento finalizado.")
            elif estado is None:
                print("Erro: nenhum atendimento aberto.")
            else:
                print(f"Erro: finalização inválida no estado '{estado}'.")

        case "S":
            print("Saindo.")
            break

        case _:
            print("Comando inválido. Use A, T, E, F ou S.")

# Questao 7

print()

n = int(input("Digite n: "))

if n < 0:
    print("Erro: n deve ser maior ou igual a zero.")
else:
    fatorial = 1
    estourou = False
    for k in range(1, n + 1):
        fatorial *= k
        if fatorial > 1_000_000:
            print(f"Passou do limite em {k}!")
            print(f"Valor acumulado até estourar: {fatorial}")
            estourou = True
            break

    if not estourou:
        print(f"{n}! = {fatorial}")

# Questao 8

print()

n = int(input("Digite n: "))

if n <= 0:
    print("Erro: n deve ser maior que zero.")
else:
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i

    if soma == n:
        classificacao = "perfeito"
    elif soma > n:
        classificacao = "abundante"
    else:
        classificacao = "deficiente"

    print(f"Soma dos divisores próprios: {soma}")
    print(f"Classificação: {classificacao}")
