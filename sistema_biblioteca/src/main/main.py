from sistema_biblioteca.src.model.admin import Admin
from sistema_biblioteca.src.model.aluno import Aluno
from sistema_biblioteca.src.model.livro import Livro
from sistema_biblioteca.src.model.biblioteca import lista_de_livros
lista_de_alunos: list[Aluno] = []
admin1 = Admin("admin", "2025")

def cabecalho():
    print("|-------------------------------------|")
    print("| Bem vindo ao sistema de biblioteca! |")
    print("|-------------------------------------|")
    print("")

def entrar_admin():
    nome = input("Login: ")
    senha = input("Senha: ")
    if nome == admin1.get_nome() and senha == admin1.get_cpf():
        print("\nBem vindo ao acesso Admin!")
        opcoes_admin()
    else:
        input(f"Não existe uma conta associada ao nome [{nome}]")

def criar_cadastro(mensagem_nome, mensagem_cpf):
    nome = input(mensagem_nome)

    cpf = ler_cpf(mensagem_cpf)

    for aluno in lista_de_alunos:
        if aluno.get_cpf() == cpf:
            input("Já existe uma conta associada a este CPF, precione ENTER para continuar.")
            return

    novo_aluno = Aluno(nome, cpf, [])
    lista_de_alunos.append(novo_aluno)
    input(f"Usuário [{novo_aluno.get_nome()}] cadastrado com sucesso! Precione ENTER para continuar.")
    return novo_aluno

def ler_cpf(mensagem):
    while True:
        cpf = input(mensagem)
        if cpf.isnumeric():
            return cpf
        else:
            input("CPF inválido. precione ENTER e tente novamente.")

def acessar_conta():
    if not lista_de_alunos:
        print("Nenhum cadastro realizado.")
        return

    cpf = ler_cpf("Informe o CPF dacastrado: ")

    for aluno in lista_de_alunos:
        if cpf == aluno.get_cpf():
            print(f"Bem vindo {aluno.get_nome()}!")
            opcoes_aluno(aluno)
            return

    input(f"Nenhum usuário com CPF: {cpf} encontrado, precione ENTER para continuar.")

def cabecalho_lista_biblioteca(mensagem):
    print(mensagem)
    print("|----------------------------------------------------------------------------|")
    print(f"| {'ID':<5} | {'TÍTULO':<25} | {'AUTOR':<20} | {'DISPONIBILIDADE':<15} |")
    print("|----------------------------------------------------------------------------|")

def cabecalho_lista_emprestados(mensagem):
    print(mensagem)
    print("|----------------------------------------------------------|")
    print(f"| {'ID':<5} | {'TÍTULO':<25} | {'AUTOR':<20} | ")
    print("|----------------------------------------------------------|")

def listar_livros(mensagem: str, lista_de_livros: list[Livro]):
    if not lista_de_livros:
        input("Nenhum livro encontrado na Biblioteca, precione ENTER para continuar.")
        return
    else:
        if mensagem == "LISTA DE LIVROS DA BIBLIOTECA":
            cabecalho_lista_biblioteca(mensagem)
            for livro in lista_de_livros:
                print(f"| {livro.get_id():<5} | {livro.titulo:<25} | {livro.autor:<20} | {livro.disponibilidade():<15} |")
            print("|----------------------------------------------------------------------------|")

        elif mensagem == "LISTA DE LIVROS EMPRESTADOS":
            cabecalho_lista_emprestados(mensagem)
            for livro in lista_de_livros:
                print(f"| {livro.get_id():<5} | {livro.titulo:<25} | {livro.autor:<20} |")
            print("|----------------------------------------------------------|")
            
def emprestar_livro(aluno):
    if not lista_de_livros:
        input("Nenhum livro encontrado na Biblioteca, precione ENTER para continuar.")
        return
    else:
        id_busca = input("Informe o ID do livro que deseja emprestar: ")
        if id_busca.isnumeric():
            for livro in lista_de_livros:
                if int(id_busca) == livro.get_id():
                    if livro.disponivel:
                        livro.disponivel = False
                        aluno.adicionar_livro(livro)
                        input(f"Livro [{livro.titulo}] emprestado com sucesso! Precione ENTER para continuar.")
                        return
                    else:
                        input(f"O livro [{livro.titulo}] não está disponível no momento, precione ENTER para voltar.")
                    return

            input(f"Nenhum livro com ID [{id_busca}] encontrado, precione ENTER para continuar.")
        else:
            print("ID inválido")



def devolver_livro(aluno):
    if not aluno.get_livros_emprestados():
        input("Não há livro(s) emprestado(s) para devolver, precione ENTER para continuar.")
        return

    id_busca = input("Informe o ID do livro que deseja devolver: ")
    if id_busca.isnumeric():
        for livro in lista_de_livros:
            if int(id_busca) == livro.get_id():
                if livro in aluno.get_livros_emprestados():
                    livro.disponivel = True
                    aluno.get_livros_emprestados().remove(livro)
                    input(f"Livro [{livro.titulo}] devolvido com sucesso! Pressione ENTER para continuar.")
                    return
                else:
                    input("Você não possui este livro, precione ENTER para continuar.")
                    return

        input(f"Nenhum livro com ID [{id_busca}] foi encontrado, precione ENTER para continuar")
    else:
        print("ID inválido.")

def devolver_tudo(lista_de_livros: list[Livro]):
    lista_de_livros.clear()


def meus_livros_emprestados(aluno):
    if not aluno.get_livros_emprestados():
        input("Lista de livros emprestados vazia, precione ENTER para continuar.")
        return
    else:
        listar_livros("LISTA DE LIVROS EMPRESTADOS", aluno.get_livros_emprestados())
        while True:
            print("-----------------------------")
            print("1 - Devolver todos os livros.")
            print("2 - Sair.")
            escolha = input()

            match escolha:
                case "1":
                    for livro in aluno.get_livros_emprestados():
                        livro.disponivel = True
                    devolver_tudo(aluno.get_livros_emprestados())
                    input("Todos os livros foram devolvidos com sucesso! Precione ENTER para continuar.")
                    break
                case "2":
                    break
                case _:
                    input("Opção inválida, precione ENTER para continuar")

def opcoes_admin():
    while True:
        opcao = {
            "1": "Adicionar livro",
            "2": "Remover livro",
            "3": "Adicionar aluno",
            "4": "Remover aluno",
            "5": "Listar aluno(s)",
            "6": "Listar livros",
            "7": "Sair"
        }
        for chave, valor in opcao.items():
            print(f"{chave}: {valor}")

        escolha = input("Escolha uma das opções acima: ")

        match escolha:
            case "1":
                admin1.adicionar_livro(lista_de_livros)
                pass
            case "2":
                admin1.remover_livro(lista_de_alunos,lista_de_livros)
            case "3":
                criar_cadastro("Informe o nome do aluno: ", "Informe o CPF do aluno: ")

            case "4":
                admin1.remover_aluno(lista_de_alunos)
            case "5":
                admin1.listar_alunos(lista_de_alunos)
            case "6":
                listar_livros("LISTA DE LIVROS DA BIBLIOTECA", lista_de_livros)
            case "7":
                break
            case _:
                input("Opção inválida, pressione ENTER para tentar navamente")




def opcoes_aluno(aluno):
    while True:
        # print("Escolha uma das opções abaixo:")
        print("")
        opcao = {
            1: "Listar livros da Biblioteca",
            2: "Emprestar livro",
            3: "Devolver livro",
            4: "Meus livros emprestados",
            5: "Encerrar sessão",
            6: "Sair da Biblioteca."
        }
        for chave, valor in opcao.items():
            print(f"{chave}: {valor}")

        while True:
            try:
                escolha_opcao = int(input("\nEscolha uma das opções acima: "))
                break
            except ValueError:
                input("Entrada inválida, precione ENTER para continuar.")
        match escolha_opcao:
            case 1:
                listar_livros("LISTA DE LIVROS DA BIBLIOTECA", lista_de_livros)
            case 2:
                emprestar_livro(aluno)
            case 3:
                devolver_livro(aluno)
            case 4:
                meus_livros_emprestados(aluno)
            case 5:
                input("Sessão encerrada com sucesso! Pressione ENTER para continuar")
                break
            case 6:
                break
            case _:
                input("Opção inválida, precione ENTER e tente novamente.")

def teste():
    pass

def main():
    while True:
        cabecalho()
        # print("Escolha uma das opções abaixo:")
        opcoes = {
            1: "Criar Cadastro",
            2: "Acessar conta",
            3: "Entrar como Administrador",
            4: "Sair"
        }
        for chave, valor in opcoes.items():
            print(f"{chave}: {valor}")

        while True:
            try:
                escolha = int(input("\nEscolha uma das opções acima: "))
                break
            except ValueError:
                input("Entrada inválida, precione ENTER e tente novamente.")

        match escolha:
            case 1:
                criar_cadastro("Informe seu nome: ", "Informe seu CPF: ")
            case 2:
                acessar_conta()
                print("Biblioteca encerrada, até mais!")
            case 3:
                entrar_admin()
            case 4:
                print("Biblioteca encerrada, até mais!")
                break
            case _:
                input("Opção inválida, precione ENTER e tente novamente.")

main()