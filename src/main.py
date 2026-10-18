"""TaskTracker - Gerenciador de tarefas via linha de comando (Bootcamp II - Fase 2)."""

tarefas = []
proximo_id = 1


def cadastrar_tarefa():
    print("\nCadastrar tarefa: funcionalidade em construção.")


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
