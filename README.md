# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastrar e visualizar tarefas do dia a dia.
Projeto desenvolvido no **Bootcamp II** — Fase 2 (Entrega Intermediária).

## Descrição funcional

O TaskTracker oferece um menu contínuo no terminal com as opções:

1. **Cadastrar tarefa** — informa título, descrição, prioridade e data limite.
2. **Listar tarefas** — mostra todas as tarefas e o total de pendentes e concluídas.
3. **Concluir tarefa** — muda o status de uma tarefa para `Concluída` a partir do ID.
4. **Sair**

Cada tarefa é guardada como um dicionário com os campos:

| Campo       | Regra                                                                 |
|-------------|-----------------------------------------------------------------------|
| ID          | Número gerado automaticamente pelo sistema (começa em 1).             |
| Título      | Obrigatório. Entradas vazias ou só com espaços são rejeitadas.        |
| Descrição   | Texto livre (opcional).                                               |
| Prioridade  | Aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`.                 |
| Data limite | Deve seguir o formato `dd/mm/aaaa` (ex: 25/09/2026).                  |
| Status      | Definido automaticamente como `Pendente` no cadastro.                 |

Quando uma entrada é inválida, o sistema mostra uma mensagem de erro e pede o dado novamente.
Se nenhuma tarefa tiver sido cadastrada, a listagem exibe `Nenhuma tarefa cadastrada.`

Exemplo de listagem:

```
[1] Ler artigo sobre Git | Prioridade: Baixa | Data: 25/09/2026 | Status: Pendente
    Descrição: Capítulos 1 a 3 do livro base

Total: 1 | Pendentes: 1 | Concluídas: 0
```

## Tecnologias utilizadas

- Python 3 (somente biblioteca padrão)
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento lógico entregue na Fase 1
└── src/
    └── main.py                   # Código-fonte principal
```

## Instalação e execução

1. Instale o [Python 3](https://www.python.org/downloads/).
2. Clone o repositório:
   ```bash
   git clone https://github.com/Nivel999/tasktracker-projeto.git
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```bash
   python src/main.py
   ```
   No Windows, também é possível usar `py src/main.py`.

## Próximos passos (Fase 3)

Empacotar a aplicação em um container Docker, adicionar testes e realizar o deploy.
