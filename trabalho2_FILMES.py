import requests
import json

# URL do WebService
url = "http://177.101.203.139/edecio/filmes.json"


def titulo(msg, traco="-", tam=50):
    print()
    print(msg)
    print(traco*tam)


def listar_serv():
    titulo(msg="Listagem de Filmes", tam=112)

    response = requests.get(url)

    filmes = json.loads(response.text)

    print("Cód. Título.............................: Gênero.......: Distribuição...................: Ano.: Público do Ano.:")

    for filme in filmes:
        print(
            f"{filme['id']:4d} {filme['titulo'][0:35]:36s} {filme['genero']:14s} {filme['empresa_distribuidora']:32s} {filme['ano_exibicao']} {filme['publico_ano_exibicao']:17}")


def filtrar_pais():
    titulo(msg="Filtro por País Produtor da Obra", tam=110)

    response = requests.get(url)

    filmes = json.loads(response.text)

    palavra = input("Informe o País: ").upper()

    print("Cód. Título.............................: Público.: País produtor da Obra.................................:")

    existe = False
    for filme in filmes:
        if palavra in filme["pais_produtor_obra"].upper():
            print(
                f"{filme['id']:4d} {filme['titulo'][0:35]:34s} {filme['publico_ano_exibicao']:11} {filme['pais_produtor_obra']:17}")
            existe = True

    if not existe:
        print(f"País Produtor da Obra: '{palavra}' não consta nos Banco")


def salvar_local():
    titulo("Salvar Filmes na Máquina Local")

    response = requests.get(url)

    filmes = json.loads(response.text)

    dados = []

    for filme in filmes:
        if filme['publico_ano_exibicao'] > 100000:
            {"id": filme['id'], "ano_exibicao": filme['ano_exibicao'], "titulo": filme['titulo'],
             "genero": filme['genero'], "pais_produtor_obra": filme['pais_produtor_obra'], "nacionalidade": filme['nacionalidade'],
             "empresa_distribuidora": filme['empresa_distribuidora'], "origem_empresa_distribuidora": filme['origem_empresa_distribuidora'],
             "publico_ano_exibicao": filme['publico_ano_exibicao'], "renda_ano_exibicao": filme['renda_ano_exibicao']}
            print(f"Salvando: {filme['titulo']}")
            dados.append(filme)

    with open("filmes.json", "w") as arq:
        json.dump(dados, arq, indent=4)


def listar_local():
    titulo(msg="Listagem de Filmes (máquina local)", tam=112)

    with open("filmes.json", "r") as arq:
        dados = json.load(arq)

    print("Cód. Título.............................: Gênero.......: Distribuição...................: Ano.: Público do Ano.:")

    for filme in dados:
        print(
            f"{filme['id']:4d} {filme['titulo'][0:35]:36s} {filme['genero']:14s} {filme['empresa_distribuidora']:32s} {filme['ano_exibicao']} {filme['publico_ano_exibicao']:17}")


def estatistica():
    titulo("Estatística Filmes")

    with open("filmes.json", "r") as arq:
        dados = json.load(arq)

    total = 0
    ano1 = 0
    ano2 = 0

    for filme in dados:
        total += filme['publico_ano_exibicao']
        if filme['ano_exibicao'] == 2018:
            ano1 += 1
        if filme['ano_exibicao'] == 2019:
            ano2 += 1

    num = len(dados)
    media = total / num

    print(f"Nº de filmes cadastrados: {num}")
    print(f"Nº de filmes lançados em 2018: {ano1}")
    print(f"Nº de filmes lançados em 2018: {ano2}")
    print(f"Público médio dos Filmes: {media:9.2f}")


def agrupar():
    titulo("Nº de Filmes por Gênero")

    with open("filmes.json", "r") as arq:
        dados = json.load(arq)

    genero = {}

    for filme in dados:
        if filme['genero'] in genero:
            genero[filme['genero']] += 1
        else:
            genero[filme['genero']] = 1

    for genero in genero.items():
        print(f"{genero[0]}: {genero[1]}")


def atividadeextra():
    titulo("Salvar Filmes na Máquina Local apenas os Filmes do Brasil")

    response = requests.get(url)

    filmes = json.loads(response.text)

    dados = []

    for filme in filmes:
        if filme["pais_produtor_obra"] == 'Brasil':
            print(
                f"{filme['id']} {filme['titulo']}")
            dados.append(filme)

    with open("filmes_brasileiros.json", "w") as arq:
        json.dump(dados, arq, indent=4)


while True:
    titulo("Programa Controle de Filmes", "=")
    print("1. Listar Filmes do servidor")
    print("2. Filtrar por País Produtor da Obra")
    print("3. Salvar Filmes na máquina local")
    print("4. Listar Filmes da máquina local")
    print("5. Estatística")
    print("6. Agrupar por gênero")
    print("7. Atividade extra")
    print("8. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar_serv()
    elif opcao == 2:
        filtrar_pais()
    elif opcao == 3:
        salvar_local()
    elif opcao == 4:
        listar_local()
    elif opcao == 5:
        estatistica()
    elif opcao == 6:
        agrupar()
    elif opcao == 7:
        atividadeextra()
    else:
        break
