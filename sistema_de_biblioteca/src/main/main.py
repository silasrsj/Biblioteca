from operator import truediv

from sistema_de_biblioteca.src.model.usuario import Usuario
from sistema_de_biblioteca.src.model.livro import Livro
from sistema_de_biblioteca.src.model.biblioteca import Biblioteca
from sistema_de_biblioteca.src.model.biblioteca import lista_de_livros
lista_de_usuarios: list[Usuario] = []

def cabecalho():
    print("|-------------------------------------|")
    print("| Bem vindo ao sistema de biblioteca! |")
    print("|-------------------------------------|")
    print("")

def criar_cadastro():
    nome = input("Informe o seu nome: ")
    while True:
        cpf = input("Informe o seu CPF: ")
        if cpf.isnumeric():
            break
        else:
            input("CPF inválido. Aperte ENTER e tente novamente.")

    novo_usuario = Usuario(nome, [])
    novo_usuario.set_cpf(cpf)
    lista_de_usuarios.append(novo_usuario)
    input(f"Usuário [ {novo_usuario.get_nome()} ] cadastrado com sucesso! Precione ENTER para continuar.")

def ler_cpf():
    cpf = input("Informe o seu CPF cadastrado: ")
    return cpf

def acessar_conta():
    if not lista_de_usuarios:
        print("Nenhum cadastro realizado.")
        return

    cpf = ler_cpf()

    for usuario in lista_de_usuarios:
        if cpf == usuario.get_cpf():
            print(f"Bem vindo {usuario.get_nome()}!")
            opcoes_usuario(usuario)
            return

    input(f"Nenhum usuário com CPF: {str(cpf).zfill(3)} encontrado, precione ENTER para continuar.")

def listar_livros():
    if not lista_de_livros:
        input("Nenhum livro encontrado na Biblioteca, precione ENTER para continuar.")
        return
    else:
        print("|--------------------------------------------------|")
        print(f"| {'TÍTULO':<15} | {'AUTOR':<12} | {'DISPONIBILIDADE':<15} |")
        print("|--------------------------------------------------|")

        for livro in lista_de_livros:
            print(f"| {livro.titulo:<15} | {livro.autor:<12} | {livro.disponibilidade():<15} |")

def emprestar_livro(usuario):
    if not lista_de_livros:
        input("Nenhum livro encontrado na Biblioteca, precione ENTER para continuar.")
        return
    else:
        nome_de_busca = input("Informe o nome do livro que deseja emprestar: ")
        for livro in lista_de_livros:
            if nome_de_busca == livro.titulo:
                if  livro.disponivel:
                    livro.disponivel = False
                    usuario.adicionar_livro(livro)
                    input(f"Livro [{nome_de_busca}] emprestado com sucesso! Precione ENTER para continuar.")
                    return
                else:
                    input(f"O livro {nome_de_busca} não está disponível no momento, precione ENTER para voltar.")
                return

        input(f"Nenhum livro [{nome_de_busca}] encontrado, precione ENTER para continuar.")

def devolver_livro(usuario):
    nome_pesquisa = input("Informe o nome do livro que deseja devolver: ")

    for livro in lista_de_livros:
        if nome_pesquisa == livro.titulo:
            livro.disponivel = True
            usuario.get_livros_emprestados().remove(livro)
            return

    input(f"Nenhum livro [{nome_pesquisa}] foi encontrado, precione ENTER para continuar")

def meus_livros_emprestados(usuario):
    if not usuario.get_livros_emprestados():
        input("Lista de livros emprestados vazia, precione ENTER para continuar.")
        return
    else:
        for livro_emprestado in usuario.get_livros_emprestados():
            print(f"Seus livros emprestados:\n {livro_emprestado.titulo}")

def opcoes_usuario(usuario):
    while True:
        print("Escolha uma das opções abaixo:")
        print("")
        opcao = {
            1: "Listar livros da Biblioteca",
            2: "Emprestar livro",
            3: "Devolver livro",
            4: "Meus livros emprestados",
            5: "Encerrar sessão",
            6: "Sair."
        }
        for chave, valor in opcao.items():
            print(f"{chave}: {valor}")
        while True:
            try:
                escolha_opcao = int(input())
                break

            except ValueError:
                input("Entrada inválida, precione ENTER e tente novamente.")

        match escolha_opcao:
            case 1:
                listar_livros()
            case 2:
                emprestar_livro(usuario)
            case 3:
                devolver_livro(usuario)

            case 4:
                meus_livros_emprestados(usuario)

            case 5:
                main()

            case 6:
                print("Biblioteca encerrada com sucesso!")
                break

            case _:
                input("Opção inválida, precione ENTER e tente novamente.")

def teste():
    pass

def main():
    cabecalho()
    while True:
        print("Escolha uma das opções abaixo:")
        opcoes = {
            1: "Criar Cadastro",
            2: "Acessar conta",
            3: "Sair"
        }
        for chave, valor in opcoes.items():
            print(f"{chave}: {valor}")

        while True:
            try:
                escolha = int(input())
                break

            except ValueError:
                input("Entrada inválida, precione ENTER e tente novamente.")
                continue

        match escolha:
            case 1:
                criar_cadastro()
            case 2:
                acessar_conta()
            case 3:
                print("Biblioteca encerrada, até mais!")
                break
            case _:
                input("Opção inválida, precione ENTER e tente novamente.")

main()