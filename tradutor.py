def pesquisar_palavra(palavra):
    # Abre o arquivo 'dicionario_ingles.txt' em modo de leitura usando a codificação UTF-8
    with open('dicionario_ingles.txt', 'r') as arquivo:
        # Lê todas as linhas do arquivo e armazena em uma lista chamada linhas
        linhas = arquivo.readlines()

    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Remove espaços em branco extras do início e do final da linha
        linha = linha.strip()
        # Verifica se a linha contém o caractere ":"
        if ":" in linha:
            # Divide a linha em partes usando ":" como separador
            partes = linha.split(":")
            # Converte a primeira parte (a palavra em inglês) para maiúsculas e remove espaços em branco extras
            palavra_encontrada = partes[0].strip().upper()
            # Junta as partes restantes (a tradução) com ":" e remove espaços em branco extras
            traducao = ":".join(partes[1:]).strip()
            # Verifica se a palavra encontrada é igual à palavra desejada (convertida para maiúsculas para fazer uma comparação sem distinção entre maiúsculas e minúsculas)
            if palavra_encontrada == palavra.upper():
                return traducao
        # Verifica se a linha contém o caractere ","
        elif "," in linha:
            # Divide a linha em partes usando "," como separador
            partes = linha.split(",")
            # Converte a primeira parte (a palavra em inglês) para maiúsculas e remove espaços em branco extras
            palavra_encontrada = partes[0].strip().upper()
            # Obtém a segunda parte (a tradução) e remove espaços em branco extras
            traducao = partes[1].strip()
            # Verifica se a palavra encontrada é igual à palavra desejada (convertida para maiúsculas para fazer uma comparação sem distinção entre maiúsculas e minúsculas)
            if palavra_encontrada == palavra.upper():
                return traducao

    # Retorna None se a palavra não for encontrada no dicionário
    return None

# Solicita ao usuário uma palavra desejada
palavra_desejada = input("Palavra desejada: ")
# Chama a função pesquisar_palavra para obter a tradução da palavra desejada
traducao = pesquisar_palavra(palavra_desejada)

# Imprime a tradução se encontrada, caso contrário, imprime uma mensagem indicando que a palavra não foi encontrada
if traducao:
    print(f"{palavra_desejada}: {traducao}")
else:
    print(f"A palavra {palavra_desejada} não foi encontrada no dicionário.")
