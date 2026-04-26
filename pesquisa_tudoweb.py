"""
Pesquisa de Satisfação - TudoWeb
Coleta e exibe o grau de satisfação de 50 clientes no atendimento.
"""

TOTAL_ENTREVISTADOS = 50

contagem_excelente = 0
contagem_bom = 0
contagem_ruim = 0

print("=" * 50)
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("=" * 50)

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")

    nome = input("Nome: ").strip()
    while not nome:
        print("Nome não pode ser vazio.")
        nome = input("Nome: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))
            if 1 <= idade <= 120:
                break
            else:
                print("Idade inválida. Informe um valor entre 1 e 120.")
        except ValueError:
            print("Informe apenas números para a idade.")

    print("Opinião sobre o atendimento:")
    print("  1 - EXCELENTE")
    print("  2 - BOM")
    print("  3 - RUIM")

    while True:
        try:
            opiniao = int(input("Escolha (1, 2 ou 3): "))
            if opiniao in (1, 2, 3):
                break
            else:
                print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Opção inválida. Digite 1, 2 ou 3.")

    if opiniao == 1:
        contagem_excelente += 1
        descricao = "EXCELENTE"
    elif opiniao == 2:
        contagem_bom += 1
        descricao = "BOM"
    else:
        contagem_ruim += 1
        descricao = "RUIM"

    print(f"Obrigado, {nome}! Resposta registrada: {descricao}")

# Exibição dos resultados
print("\n" + "=" * 50)
print("        RESULTADO DA PESQUISA")
print("=" * 50)
print(f"Total de entrevistados : {TOTAL_ENTREVISTADOS}")
print(f"Respostas EXCELENTE    : {contagem_excelente}")
print(f"Respostas BOM          : {contagem_bom}")
print(f"Respostas RUIM         : {contagem_ruim}")
print("=" * 50)
