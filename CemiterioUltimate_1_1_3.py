import datetime
import json
import os

REGISTROS_JSON_FILE = 'registros.json'

registros = []


def verificar_arquivo_existente():
    return os.path.exists(REGISTROS_JSON_FILE)


def carregar_registros():
    if verificar_arquivo_existente():
        if not len(registros):
            with open(REGISTROS_JSON_FILE, "r") as file:
                registros.extend(json.load(file))
    else:
        criar_arquivo_inicial()


def criar_arquivo_inicial():
    registros_iniciais = [
        {'numero_cova': 1, 'nome_defunto': 'João da Silva', 'nome_responsavel': 'Maria Silva',
            'data_falecimento': '30/05/2023', 'data_cadastro': datetime.datetime.now().strftime('%d/%m/%Y'), 'data_atualizacao': None},
        {'numero_cova': 2, 'nome_defunto': 'José Pereira', 'nome_responsavel': 'Ana Pereira',
            'data_falecimento': '31/05/2023', 'data_cadastro': datetime.datetime.now().strftime('%d/%m/%Y'), 'data_atualizacao': None},
        {'numero_cova': 3, 'nome_defunto': 'Maria Santos', 'nome_responsavel': 'Carlos Santos',
            'data_falecimento': '01/06/2023', 'data_cadastro': datetime.datetime.now().strftime('%d/%m/%Y'), 'data_atualizacao': None},
        {'numero_cova': 4, 'nome_defunto': 'Antônio Oliveira', 'nome_responsavel': 'Sandra Oliveira',
            'data_falecimento': '01/06/2023', 'data_cadastro': datetime.datetime.now().strftime('%d/%m/%Y'), 'data_atualizacao': None},
        {'numero_cova': 5, 'nome_defunto': 'Fernanda Souza', 'nome_responsavel': 'Ricardo Souza',
            'data_falecimento': '02/06/2023', 'data_cadastro': datetime.datetime.now().strftime('%d/%m/%Y'), 'data_atualizacao': None}
    ]
    registros.extend(registros_iniciais)
    salvar_registros()


def salvar_registros():
    with open(REGISTROS_JSON_FILE, 'w') as file:
        json.dump(registros, file, indent=4)


def cadastrar():
    print("\n"*2)
    print("CADASTRO DE NOVO CLIENTE PARA O CEMITÉRIO\n\n")
    numero_cova = input("Número da Cova: ")

    while not numero_cova.isdigit():
        print("Erro: Número da Cova deve conter apenas números.\n")
        numero_cova = input("Número da Cova: ")

    nome_defunto = input("Nome do Defunto: ")
    nome_responsavel = input("Nome do Responsável: ")
    data_falecimento = input("Data do Falecimento (AAAA-MM-DD): ")
    print("\n"*2)

    if not numero_cova or not nome_defunto or not nome_responsavel or not data_falecimento:
        print("\n"*2)
        print("Erro: Todos os campos devem ser preenchidos.\n")
        return

    registro = {
        'numero_cova': numero_cova,
        'nome_defunto': nome_defunto,
        'nome_responsavel': nome_responsavel,
        'data_falecimento': formatar_data(data_falecimento),
        'data_cadastro': str(datetime.datetime.now()),
        'data_atualizacao': None
    }

    registros.append(registro)
    salvar_registros()
    titulo()
    print("\n"*2)
    print("Registro cadastrado com sucesso!\n")
    x = input("Aperte enter para continuar...")


def formatar_data(data):
    data_obj = datetime.datetime.strptime(data, '%Y-%m-%d')
    return data_obj.strftime('%d/%m/%Y')


def buscar():
    termo = input(
        "Digite o número da cova, nome completo ou parcial ou aperte (ENTER) para listar tudo: ").lower()

    resultados = []

    for registro in registros:
        if str(registro['numero_cova']) == termo or termo in registro['nome_defunto'].lower() or termo in registro['nome_responsavel'].lower():
            resultados.append(registro)

    if resultados:
        print("\n"*2)
        print("Resultados da busca:")
        print("\n")
        for i, registro in enumerate(resultados, start=1):
            print(
                f"{i}. Número da Cova: {registro['numero_cova']}, Nome do Defunto: {registro['nome_defunto']}, Nome do Responsável: {registro['nome_responsavel']}, Data do Falecimento: {registro['data_falecimento']}")

        print("\n")

        selecao = input(
            "Selecione o número do registro para exibir os detalhes, ou 'voltar' para retornar ao menu anterior: ")
        if selecao.isdigit() and int(selecao) <= len(resultados):
            registro_selecionado = resultados[int(selecao) - 1]
            print("\n")
            print("\nDetalhes do Registro:")
            print("Número da Cova:", registro_selecionado['numero_cova'])
            print("Nome do Defunto:", registro_selecionado['nome_defunto'])
            print("Nome do Responsável:",
                  registro_selecionado['nome_responsavel'])
            print("Data do Falecimento:",
                  registro_selecionado['data_falecimento'])
            print("\n")
            print("Criado em: ",
                  registro_selecionado['data_cadastro'])
            print("Ultima Atualização: ",
                  registro_selecionado['data_atualizacao'])
            print("\n")

            opcao = input(
                "Escolha 'e' para editar ou 'd' para deletar o registro, ou qualquer outra tecla para volar ao menu: ")
            if opcao == 'e':
                editar_registro(registro_selecionado)
            elif opcao == 'd':
                titulo()
                e = input("Deseja realmente remover o registro? (s/n) : ").lower()
                
                if e == "s":
                    deletar_registro(registro_selecionado)
                    
            else:
                print("Opção inválida.")
        elif selecao.lower() == 'voltar':
            main()
        else:
            print("Seleção inválida.")
    else:
        print("\n"*2)
        print("Nenhum resultado encontrado.")

        buscar()


def editar_registro(registro):
    print("\n")
    print("Editar Registro:")
    print("Deixe em branco para manter o valor original.")
    print("\n")

    novo_numero_cova = input("Novo Número da Cova: ")

    while not novo_numero_cova.isdigit() and novo_numero_cova:
        print("Erro: Número da Cova deve conter apenas números.\n")
        novo_numero_cova = input("Novo Número da Cova: ")

    novo_nome_defunto = input("Novo Nome do Defunto: ")
    novo_nome_responsavel = input("Novo Nome do Responsável: ")
    nova_data_falecimento = input("Nova Data do Falecimento: ")

    if novo_numero_cova:
        registro['numero_cova'] = novo_numero_cova
    if novo_nome_defunto:
        registro['nome_defunto'] = novo_nome_defunto
    if novo_nome_responsavel:
        registro['nome_responsavel'] = novo_nome_responsavel
    if nova_data_falecimento:
        registro['data_falecimento'] = nova_data_falecimento

    registro['data_atualizacao'] = str(datetime.datetime.now())

    print("\n"*2)
    print("Novos Dados:")
    print("Número da Cova:", registro['numero_cova'])
    print("Nome do Defunto:", registro['nome_defunto'])
    print("Nome do Responsável:", registro['nome_responsavel'])
    print("Data do Falecimento:", registro['data_falecimento'])
    print("\n"*2)

    confirmacao = input("Deseja confirmar as alterações? (S/N): ")
    if confirmacao.lower() == 's':
        salvar_registros()
        print("\n"*2)
        titulo()
        print("Registro atualizado com sucesso!")
        x = input("Aperte enter para continuar....")
    else:
        print("\n"*2)
        titulo()
        print("Alterações descartadas.")
        x = input("Aperte enter para continuar....")


def deletar_registro(registro):
    registros.remove(registro)
    salvar_registros()
    titulo()
    print("\n"*2)
    print("Registro deletado com sucesso!")
    x = input("Aperte enter para continuar....")
    


def exibir_menu():
    print("\n"*2)
    print("==== Menu Principal =====\n")
    print("1. Cadastrar")
    print("2. Buscar, Alterar ou Remover")
    print("3. Exibir Matriz")
    print("4. Sair \n")


def exibir_matriz():
    print(registros)
    print("\n")
    x = input("Aperte qualquer tecla para continuar...")


def limpar_tela():
    if os.name == 'nt':  # Verifica se é Windows
        os.system('cls')
    else:  # Outros sistemas (macOS, Linux)
        os.system('clear')


def titulo():
    limpar_tela()
    print("\n")
    print("++++ Cemetery Ultimate Ver. 1.1.3 ++++")
    print("Programa Desenvolvido por: \nAmanda Gonçalves \nFilipe Duarte  \nWilton Oliveira\n")
    print("\n")


def main():
    carregar_registros()

    while True:
        titulo()
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo()
            cadastrar()
        elif opcao == '2':
            titulo()
            buscar()
        elif opcao == '3':
            titulo()
            exibir_matriz()
        elif opcao == '4':
            limpar_tela()
            print("Obrigado por usar o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
