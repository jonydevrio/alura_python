# ===== LIÇÃO 1: TIPOS DE DADOS E VARIÁVEIS =====
print("=" * 50)
print("LIÇÃO 1: TIPOS DE DADOS E VARIÁVEIS")
print("=" * 50)

# Criando variáveis de diferentes tipos
nome = "João"          # Tipo STRING (str)
idade = 25             # Tipo INTEIRO (int)
altura = 1.75          # Tipo DECIMAL (float)
estudante = True       # Tipo BOOLEANO (bool)

print(f"\nMeu nome é {nome}")
print(f"Tenho {idade} anos")
print(f"Minha altura é {altura} metros")
print(f"Sou estudante: {estudante}")

print("\n📌 APRENDIZADO: Variáveis armazenam dados em tipos diferentes")
print("   - str: texto, entre aspas")
print("   - int: números inteiros, sem ponto decimal")
print("   - float: números decimais, com ponto")
print("   - bool: verdadeiro (True) ou falso (False)")
input("\n[Pressione ENTER para continuar...]")

# ===== LIÇÃO 2: OPERAÇÕES MATEMÁTICAS =====
print("\n" + "=" * 50)
print("LIÇÃO 2: OPERAÇÕES MATEMÁTICAS")
print("=" * 50)

numero1 = 15
numero2 = 4

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2
potencia = numero1 ** 2

print(f"\nNúmero 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"\nSoma: {numero1} + {numero2} = {soma}")
print(f"Subtração: {numero1} - {numero2} = {subtracao}")
print(f"Multiplicação: {numero1} × {numero2} = {multiplicacao}")
print(f"Divisão: {numero1} ÷ {numero2} = {divisao}")
print(f"Divisão Inteira: {numero1} // {numero2} = {divisao_inteira}")
print(f"Resto (Módulo): {numero1} % {numero2} = {resto}")
print(f"Potência: {numero1}² = {potencia}")

print("\n📌 APRENDIZADO: Operadores matemáticos em Python")
print("   + (soma)  - (subtração)  * (multiplicação)")
print("   / (divisão)  // (divisão inteira)  % (resto)")
print("   ** (potência)")
input("\n[Pressione ENTER para continuar...]")

# ===== LIÇÃO 3: CONCATENAÇÃO E F-STRINGS =====
print("\n" + "=" * 50)
print("LIÇÃO 3: CONCATENAÇÃO E F-STRINGS")
print("=" * 50)

primeiro_nome = "Maria"
sobrenome = "Silva"
ano_nascimento = 1995

# Concatenação tradicional
apresentacao1 = "Olá, meu nome é " + primeiro_nome + " " + sobrenome

# F-string (forma moderna)
idade_calc = 2025 - ano_nascimento
apresentacao2 = f"Olá! Meu nome é {primeiro_nome} {sobrenome} e tenho {idade_calc} anos."

print(f"\nConcatenação tradicional:")
print(apresentacao1)

print(f"\nUsando F-String:")
print(apresentacao2)

print("\n📌 APRENDIZADO: F-Strings")
print("   - Forma moderna de juntar texto e variáveis")
print("   - Use f'texto {variável}' para interpolação")
print("   - Mais legível e poderosa que concatenação com +")
input("\n[Pressione ENTER para continuar...]")

# ===== LIÇÃO 4: MANIPULAÇÃO DE STRINGS =====
print("\n" + "=" * 50)
print("LIÇÃO 4: MANIPULAÇÃO DE STRINGS")
print("=" * 50)

texto_original = "  Python é INCRÍVEL  "
print(f"\nTexto original: '{texto_original}'")

# Método lower() - converte para minúsculas
texto_minusculo = texto_original.lower()
print(f"\nMétodo lower(): '{texto_minusculo}'")

# Método upper() - converte para maiúsculas
texto_maiusculo = texto_original.upper()
print(f"Método upper(): '{texto_maiusculo}'")

# Método strip() - remove espaços das extremidades
texto_sem_espacos = texto_original.strip()
print(f"Método strip(): '{texto_sem_espacos}'")

# Método replace() - substitui um texto por outro
texto_modificado = texto_original.replace("INCRÍVEL", "FANTÁSTICO")
print(f"Método replace(): '{texto_modificado}'")

# Combinando métodos
texto_processado = texto_original.strip().lower().replace("python", "PYTHON")
print(f"Combinando métodos: '{texto_processado}'")

print("\n📌 APRENDIZADO: Métodos de String")
print("   - lower(): converte tudo para minúsculas")
print("   - upper(): converte tudo para maiúsculas")
print("   - strip(): remove espaços no início e fim")
print("   - replace(velho, novo): substitui texto")
print("   - Métodos podem ser combinados com ponto (.)")
input("\n[Pressione ENTER para continuar...]")

# ===== LIÇÃO 5: INPUT DO USUÁRIO =====
print("\n" + "=" * 50)
print("LIÇÃO 5: RECEBENDO DADOS DO USUÁRIO")
print("=" * 50)

print("\n🔹 Primeira vez: responda com uma cor")
cor_usuario = input("Qual é sua cor favorita? ").strip().lower()
print(f"Você respondeu: {cor_usuario}")
print(f"Em maiúsculas: {cor_usuario.upper()}")

print("\n🔹 Segunda vez: responda com um número")
numero_usuario = input("Digite um número inteiro: ")
numero_convertido = int(numero_usuario)
numero_dobrado = numero_convertido * 2
print(f"O número {numero_convertido} dobrado é {numero_dobrado}")

print("\n🔹 Terceira vez: responda com altura")
altura_usuario = input("Qual é sua altura em metros? (ex: 1.70): ")
altura_float = float(altura_usuario)
print(f"Sua altura é {altura_float}m, em centímetros: {altura_float * 100}cm")

print("\n📌 APRENDIZADO: Input do Usuário")
print("   - input('mensagem') recebe texto do usuário")
print("   - input() sempre retorna STRING, mesmo se digitar número")
print("   - Use int() para converter em inteiro")
print("   - Use float() para converter em decimal")
input("\n[Pressione ENTER para continuar...]")

# ===== LIÇÃO 6: CONDICIONAIS IF =====
print("\n" + "=" * 50)
print("LIÇÃO 6: CONDICIONAIS IF")
print("=" * 50)

print("\n🔹 Testando condicionais com sua cor favorita")
cor = input("Digite uma cor: ").strip().lower()

if cor == "azul":
    print("Você escolheu azul! Cor do céu e do mar.")
elif cor == "vermelho":
    print("Você escolheu vermelho! Cor de energia e paixão.")
elif cor == "verde":
    print("Você escolheu verde! Cor da natureza.")
else:
    print(f"A cor {cor} é interessante também!")

print("\n🔹 Testando condicionais com números")
idade_teste = int(input("Digite sua idade: "))

if idade_teste < 13:
    print("Você é uma criança.")
elif idade_teste < 18:
    print("Você é um adolescente.")
elif idade_teste < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

print("\n📌 APRENDIZADO: Condicionais IF")
print("   - if: executa se a condição for True")
print("   - elif: testa outra condição (else if)")
print("   - else: executa se nenhuma condição for True")
print("   - Operadores: == (igual), != (diferente)")
print("             < (menor), > (maior), <= (menor/igual)")
input("\n[Pressione ENTER para continuar...]")

# ===== LIÇÃO 7: PROJETO PRÁTICO =====
print("\n" + "=" * 50)
print("LIÇÃO 7: PROJETO PRÁTICO")
print("=" * 50)

print("\n🎯 Vamos criar um programa que calcula seu IMC!")
print("(Índice de Massa Corporal)\n")

nome_imc = input("Como você se chama? ").strip()
peso = float(input("Qual é seu peso em kg? "))
altura_imc = float(input("Qual é sua altura em m? (ex: 1.70) "))

imc = peso / (altura_imc ** 2)
imc_arredondado = round(imc, 2)

print(f"\n{'='*40}")
print(f"Resultado da Avaliação de {nome_imc.upper()}")
print(f"{'='*40}")
print(f"Peso: {peso} kg")
print(f"Altura: {altura_imc} m")
print(f"IMC: {imc_arredondado}")

if imc_arredondado < 18.5:
    categoria = "Abaixo do peso"
elif imc_arredondado < 25:
    categoria = "Peso normal"
elif imc_arredondado < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

print(f"Categoria: {categoria}")
print(f"{'='*40}")
