from sistema_de_biblioteca.src.model.usuario import Usuario
from sistema_de_biblioteca.src.model.livro import Livro
from sistema_de_biblioteca.src.model.biblioteca import lista_de_livros
lista_de_usuarios: list[Usuario] = []

def cabecalho():
    print("|-------------------------------------|")
    print("| Bem vindo ao sistema de biblioteca! |")
    print("|-------------------------------------|")
    print("")

def criar_cadastro():
    nome = input("Informe o seu nome: ")

    cpf = ler_cpf("Informe seu CPF: ")

    for usuario in lista_de_usuarios:
        if usuario.get_cpf() == cpf:
            input("Já existe uma conta associada a este CPF, pressione ENTER para continuar.")
            return

    novo_usuario = Usuario(nome, [])
    novo_usuario.set_cpf(cpf)
    lista_de_usuarios.append(novo_usuario)
    input(f"Usuário [ {novo_usuario.get_nome()} ] cadastrado com sucesso! Pressione ENTER para continuar.")

def ler_cpf(mensagem):
    while True:
        cpf = input(mensagem)
        if cpf.isnumeric():
            return cpf
        else:
            input("CPF inválido. pressione ENTER e tente novamente.")

def acessar_conta():
    if not lista_de_usuarios:
        print("Nenhum cadastro realizado.")
        return

    cpf = ler_cpf("Informe o CPF cadastrado: ")

    for usuario in lista_de_usuarios:
        if cpf == usuario.get_cpf():
            print(f"Bem vindo {usuario.get_nome()}!")
            opcoes_usuario(usuario)
            return

    input(f"Nenhum usuário com CPF: {cpf} encontrado, pressione ENTER para continuar.")

def cabecalho_lista_biblioteca(mensagem):
    print(mensagem)
    print("|--------------------------------------------------|")
    print(f"| {'TÍTULO':<15} | {'AUTOR':<12} | {'DISPONIBILIDADE':<15} |")
    print("|--------------------------------------------------|")

def cabecalho_lista_emprestados(mensagem):
    print(mensagem)
    print("|--------------------------------|")
    print(f"| {'TÍTULO':<15} | {'AUTOR':<12} | ")
    print("|--------------------------------|")

def listar_livros(mensagem: str, lista_de_livros: list[Livro]):
    if not lista_de_livros:
        input("Nenhum livro encontrado na Biblioteca, pressione ENTER para continuar.")
        return
    else:
        if mensagem == "LISTA DE LIVROS DA BIBLIOTECA":
            cabecalho_lista_biblioteca(mensagem)
            for livro in lista_de_livros:
                print(f"| {livro.titulo:<15} | {livro.autor:<12} | {livro.disponibilidade():<15} |")
            print("|--------------------------------------------------|")

        elif mensagem == "LISTA DE LIVROS EMPRESTADOS":
            cabecalho_lista_emprestados(mensagem)
            for livro in lista_de_livros:
                print(f"| {livro.titulo:<15} | {livro.autor:<12} |")
            print("|--------------------------------|")
            
def emprestar_livro(usuario):
    if not lista_de_livros:
        input("Nenhum livro encontrado na Biblioteca, pressione ENTER para continuar.")
        return
    else:
        nome_de_busca = input("Informe o nome do livro que deseja emprestar: ")
        for livro in lista_de_livros:
            if nome_de_busca == livro.titulo:
                if  livro.disponivel:
                    livro.disponivel = False
                    usuario.adicionar_livro(livro)
                    input(f"Livro [{nome_de_busca}] emprestado com sucesso! pressione ENTER para continuar.")
                    return
                else:
                    input(f"O livro {nome_de_busca} não está disponível no momento, pressione ENTER para voltar.")
                return

        input(f"Nenhum livro [{nome_de_busca}] encontrado, pressione ENTER para continuar.")

def devolver_livro(usuario):
    if not usuario.get_livros_emprestados():
        input("Não há livro(s) emprestado(s) para devolver, pressione ENTER para continuar.")
        return

    nome_pesquisa = input("Informe o nome do livro que deseja devolver: ")

    for livro in lista_de_livros:
        if nome_pesquisa == livro.titulo:
            if livro in usuario.get_livros_emprestados():
                livro.disponivel = True
                usuario.get_livros_emprestados().remove(livro)
                return
            else:
                input("Você não possui este livro, pressione ENTER para continuar.")
                return

    input(f"Nenhum livro [{nome_pesquisa}] foi encontrado, pressione ENTER para continuar")

def devolver_tudo(lista_de_livros: list[Livro]):
    lista_de_livros.clear()


def meus_livros_emprestados(usuario):
    if not usuario.get_livros_emprestados():
        input("Lista de livros emprestados vazia, pressione ENTER para continuar.")
        return
    else:
        listar_livros("LISTA DE LIVROS EMPRESTADOS", usuario.get_livros_emprestados())
        while True:
            print("-----------------------------")
            print("1 - Devolver todos os livros.")
            print("2 - Sair.")
            escolha = input()

            match escolha:
                case "1":
                    for livro in usuario.get_livros_emprestados():
                        livro.disponivel = True
                    devolver_tudo(usuario.get_livros_emprestados())
                    input("Todos os livros foram devolvidos com sucesso! Pressione ENTER para continuar.")
                    break
                case "2":
                    break
                case _:
                    input("Opção inválida, pressione ENTER para continuar")

def opcoes_usuario(usuario):
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
                input("Entrada inválida, pressione ENTER para continuar.")
    
        match escolha_opcao:
            case 1:
                listar_livros("LISTA DE LIVROS DA BIBLIOTECA", lista_de_livros)
            case 2:
                emprestar_livro(usuario)
            case 3:
                devolver_livro(usuario)

            case 4:
                meus_livros_emprestados(usuario)

            case 5:
                input("Sessão encerrada com sucesso! Pressione ENTER para continuar")
                main()

            case 6:
                break

            case _:
                input("Opção inválida, pressione ENTER e tente novamente.")

def teste():
    pass

def main():
    cabecalho()
    while True:
        # print("Escolha uma das opções abaixo:")
        opcoes = {
            1: "Criar Cadastro",
            2: "Acessar conta",
            3: "Sair"
        }
        for chave, valor in opcoes.items():
            print(f"{chave}: {valor}")

        while True:
            try:
                escolha = int(input("\nEscolha uma das opções acima: "))
                break

            except ValueError:
                input("Entrada inválida, pressione ENTER e tente novamente.")

        match escolha:
            case 1:
                criar_cadastro()
            case 2:
                acessar_conta()
                print("Biblioteca encerrada, até mais!")
                break
            case 3:
                print("Biblioteca encerrada, até mais!")
                break
            case _:
                input("Opção inválida, pressione ENTER e tente novamente.")

main()