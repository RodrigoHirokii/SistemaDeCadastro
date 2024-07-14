print("Bem vindos a empresa do Rodrigo Hiroki Shimizu")

listaDeFuncionarios = []
idGlobal = 4895885


def cadastar_funcionario(id):
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionarioAdd = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    listaDeFuncionarios.append(funcionarioAdd.copy())


def consultar_funcionarios():
    while True:
        print("-" * 10 + "-" * 10)
        print("-" * 10 + "MENU CONSULTAR FUNCIONÁRIO " + "-" * 10)
        print("Escolha a opção desejada: ")
        print("1 - Consultar Todos os Funcionários: ")
        print("2 - Consultar Funcionário por id ")
        print("3 - Consultar Funcionário(s) por setor ")
        print("4 - Retornar")

        opcaoSelecionada = input(">>: ")
        print("---------------")

        if (opcaoSelecionada == "1"):
            if listaDeFuncionarios:
                for funcionario in listaDeFuncionarios:
                    print("id: {} nome: {} setor: {} salario: {:.2f}".format(funcionario['id'], funcionario['nome'],
                                                                             funcionario['setor'],
                                                                             funcionario['salario']))
            else:
                print("No momento não possui funcionários cadastrados")

        elif (opcaoSelecionada == "2"):
            consultar_id = int(input("Digite o id do funcionário: "))
            acharFuncionario = False

            for funcionario in listaDeFuncionarios:
                if funcionario['id'] == consultar_id:
                    print("id: {} nome: {} setor: {} salario: {:.2f}".format(funcionario['id'], funcionario['nome'],
                                                                             funcionario['setor'],
                                                                             funcionario['salario']))
                    acharFuncionario = True
                    break

            if not acharFuncionario:
                print("Funcionário não cadastrado no sistema!!")
                break

        elif (opcaoSelecionada == "3"):
            setor_funcionarios = input("Consultar Funcionários(s) por setor: ")
            funcionarios_disponivies = False

            for funcionario in listaDeFuncionarios:
                if funcionario['setor'].lower() == setor_funcionarios.lower():
                    print("id: {} nome: {} setor: {} salario: {:.2f}".format(funcionario['id'], funcionario['nome'],
                                                                             funcionario['setor'],
                                                                             funcionario['salario']))
                    funcionarios_disponivies = True
            if not funcionarios_disponivies:
                print("Não há funcionarios disponíveis nesse setor no momento!!!")
        elif (opcaoSelecionada == "4"):
            print("Indo para o menu principal")
            return
        else:
            print("Ocorreu um erro!!!")


def remover_funcionario():
    while True:
        removerIdFuncionario = int(input("Digite o id do funcionário a ser removido: "))
        funcionarioIdentificado = False

        for funcionario in listaDeFuncionarios:
            if funcionario['id'] == removerIdFuncionario:
                listaDeFuncionarios.remove(funcionario)
                print("O funcionário que você digitou foi removido com sucesso!!!")
                funcionarioIdentificado = True
                break  # Adiciona esta linha para sair do loop após a remoção
        if not funcionarioIdentificado:
            print("Você digitou o ID errado!! Ou o funcionarío não está cadastrado")
        else:
            break


while True:
    print("-" * 10 + "-" * 10)
    print("-" * 10 + "MENU PRINCIPAL " + "-" * 10)
    print("1 - Cadastrar Funcionários: ")
    print("2 - Consultar Funcionário(s): ")
    print("3 - Remover Funcionário: ")
    print("4 - Sair: ")

    opcaoSelecionada = input("Escolha a opção desejada: ")

    if (opcaoSelecionada == "1"):
        idGlobal += 1
        cadastar_funcionario(idGlobal)

    elif (opcaoSelecionada == "2"):
        consultar_funcionarios()

    elif (opcaoSelecionada == "3"):
        remover_funcionario()

    elif (opcaoSelecionada == "4"):
        print("Você selecionou a opção de sair do programa")
        break
    else:
        print("Você digitou uma opção inválida")
