
import secrets
import string

print("==============================")
print("      GERADOR DE SENHAS")
print("==============================")

# Solicita o tamanho da senha e valida a entrada
while True:
    try:
        tamanho = int(input("Quantos caracteres deseja na senha? "))

        if 1 <= tamanho <= 128:
            break

        print("Erro: digite um valor entre 1 e 128!")

    except ValueError:
        print("Erro: você precisa digitar um número!")

# Reúne letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera a senha
senha = ""

for i in range(tamanho):
    senha += secrets.choice(caracteres)

# Exibe o resultado
print("\nSua senha gerada é:")
print(senha)
