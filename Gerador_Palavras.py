import nltk
nltk.download('punkt')

artigos = "artigos.txt"
with open(artigos, 'r') as f: # 'r' de read e o 'f' de file

    def separa_palavras(lista_tokens):
        lista_palavras = []
        for token in lista_tokens:
            if token.isalpha():  # acrescentaremos apenas os itens que são realmente vocábulos.
                lista_palavras.append(token)
        return lista_palavras

    def normalize(lista_palavras):
        lista_normalizada = []
        for palavra in lista_palavras:
            lista_normalizada.append(palavra.lower())  # transformar todas as palavras em minuscula
        return lista_normalizada

    def insere_letras(fatias):
        novas_palavras = []
        letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
        for E, D in fatias:
            for letra in letras:
                novas_palavras.append(E + letra + D)
        return novas_palavras

    def deletando_caracteres(fatias):
        novas_palavras = []
        for E, D in fatias:
            novas_palavras.append(E + D[1:])
        return novas_palavras

    def troca_letra(fatias):
        novas_palavras = []
        letras = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìóòõôúùûç'
        for E, D in fatias:
            for letra in letras:
                novas_palavras.append(E + letra + D[1:])
        return novas_palavras

    def inverte_letra(fatias): # função para inverter letras, usa condicional if.
        novas_palavras = []
        for E, D in fatias:
            if len(D) > 1:
                novas_palavras.append(E + D[1] + D[0] + D[2:])
        return novas_palavras

    def gerador_palavras(palavra):
        fatias = []
        for i in range(len(palavra)+1):
            fatias.append((palavra[:i],palavra[i:]))
        palavras_geradas = insere_letras(fatias)
        palavras_geradas += deletando_caracteres(fatias)
        palavras_geradas += troca_letra(fatias)
        palavras_geradas += inverte_letra(fatias)
        return palavras_geradas

palavra_exemplo = "Verde" # digite a palavra e teste
palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)




