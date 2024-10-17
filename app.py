import os

restaurantes = []


def exibir_nome_do_programa():
    print(
        """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""
    )


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")


def finalizar_app():
    exibir_subtitulo("Finalizando o app")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system("clear")

    linha = "*" * (len(texto))

    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """
    Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    """

    exibir_subtitulo("Cadastro de novos restaurantes\n")

    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")

    dados_do_restaurante = {
        "nome": nome_restaurante,
        "categoria": categoria,
        "ativo": False,
    }

    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes\n")

    print(f"{'Nome do restaurante'.ljust(21)} | {"Categoria".ljust(20)} | {"Status"}")

    for restaurante in restaurantes:
        print(
            f".{restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'Ativado' if restaurante['ativo'] else 'Desativado'}"
        )

    voltar_ao_menu_principal()


def alternar_estado_do_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")

    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alternar o estado: "
    )

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True

            restaurante["ativo"] = not restaurante["ativo"]

            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com sucesso"
                if restaurante["ativo"]
                else f"O restaurante foi desativado com sucesso"
            )

            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as err:
        if err != None:
            print(f"\nErro: {err}\n")

        opcao_invalida()


def main():
    os.system("clear")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
