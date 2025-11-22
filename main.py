# ==========================================
# SISTEMA CLÍNICA VIDA+
# Desenvolvido por: Lucas Viana
# Projeto Integrado - ADS
# ==========================================

# Lista para armazenar os pacientes
pacientes = []

def cadastrar_paciente():
    print("\n=== CADASTRO DE PACIENTE ===")
    nome = input("Nome do paciente: ").strip()
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("⚠️ Erro: idade deve ser um número inteiro!")
        return
    telefone = input("Telefone: ").strip()
    paciente = {"nome": nome, "idade": idade, "telefone": telefone}
    pacientes.append(paciente)
    print(f"✅ Paciente {nome} cadastrado com sucesso!")

def ver_estatisticas():
    print("\n=== ESTATÍSTICAS ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda x: x["idade"])
    mais_velho = max(pacientes, key=lambda x: x["idade"])
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f} anos")
    print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente():
    print("\n=== BUSCA DE PACIENTE ===")
    nome = input("Digite o nome do paciente: ").strip().lower()
    encontrados = [p for p in pacientes if nome in p["nome"].lower()]
    if encontrados:
        for p in encontrados:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print("Paciente não encontrado.")

def listar_pacientes():
    print("\n=== LISTA DE PACIENTES ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")

# Loop principal do sistema
while True:
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        ver_estatisticas()
    elif opcao == "3":
        buscar_paciente()
    elif opcao == "4":
        listar_pacientes()
    elif opcao == "5":
        print("👋 Encerrando o sistema. Até logo!")
        break
    else:
        print("⚠️ Opção inválida! Tente novamente.")
