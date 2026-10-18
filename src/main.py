"""TaskTracker - Gerenciador de tarefas via linha de comando (Bootcamp II - Fase 2)."""

from datetime import datetime

PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

tarefas = []
proximo_id = 1


def ler_titulo():
    """Pede o título até que o usuário digite algo que não seja vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar em branco. Tente novamente.")


def ler_prioridade():
    """Pede a prioridade até que seja Alta, Média (ou Media) ou Baixa."""
    while True:
        prioridade = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if prioridade in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[prioridade]
        print("Erro: prioridade inválida. Digite apenas Alta, Média ou Baixa.")


def ler_data():
    """Pede a data limite até que siga o formato dd/mm/aaaa."""
    while True:
        data = input("Data limite (dd/mm/aaaa): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: data inválida. Use o formato dd/mm/aaaa (ex: 25/09/2026).")


def cadastrar_tarefa():
    global proximo_id

    print("\n--- Cadastrar tarefa ---")
    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data()

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    proximo_id += 1
    print(f"\nTarefa registrada com sucesso! (ID {tarefa['id']})")


def listar_tarefas():
    print("\nListar tarefas: funcionalidade em construção.")


def concluir_tarefa():
    print("\nConcluir tarefa: funcionalidade em construção.")


def exibir_menu():
    print("\n========== TASKTRACKER ==========")
    print("[1] Cadastrar tarefa")
    print("[2] Listar tarefas")
    print("[3] Concluir tarefa")
    print("[4] Sair")
    print("=================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            print("Finalizando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")


if __name__ == "__main__":
    main()
