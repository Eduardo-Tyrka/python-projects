# jogo da forca

import random

programWorking = True

listOfWords = ["abacaxi", "tigre", "computador", "beleza", "girafa", "sapato", "amizade", "bexiga", "cachorro", "flor", "carro", "relogio", "abobora", "janela", "musica", "escola", "aviao", "chave", "televisao", "caderno", "oceano", "verde", "bola", "passaro", "floresta", "telefone", "cachoeira", "esmalte", "pintura", "pessoa", "livro", "pato", "chapeu", "futebol", "lanterna", "foca", "pintinho", "roda", "torneira", "cavalo", "serpente", "gato", "bolo", "oculto", "refrigerante", "coracao", "piramide", "estrada", "sol", "nuvem", "guitarra", "amor", "lua", "estrela", "noite", "dolar", "espanhol", "festa", "sabo", "urso", "abacate", "papel", "esmalte", "coelho", "dente", "jacare", "lampada", "flor", "pirata", "gelo", "horizonte", "geleia", "campo", "vento", "peixe", "tinta", "pomada", "abacaxi", "carne", "vacina", "flores", "palmeira", "melancia", "sorriso", "verao", "banco", "calor", "chuva", "livros", "radio", "abismo", "cabelo", "rosa", "bico", "feijao", "sombra", "caixa", "pilha", "sorvete", "estrela", "viagem", "moeda", "caminho", "perigo", "cultura", "arco", "amarelo", "quadrado", "flutuar", "padeiro", "rocha", "minhoca", "mercado", "boia", "templo", "bicho", "amigo", "concha", "governo", "colina", "leao", "tinta", "foca", "velocidade", "tucano", "mel", "oculos", "resposta", "serra", "ponte", "pequeno", "violao"]
firstRound = True

while programWorking:

    if firstRound:
        randonNumber = random.randint(0, len(listOfWords) - 1)
        realWord = listOfWords[randonNumber]
        rightGuessedLetters = ["_" for x in range(len(realWord))]
        wrongGuessedLetters = []
        firstRound = False

    
    for i in rightGuessedLetters:
        status = ' '.join(rightGuessedLetters)

    print("Jogo da Forca")
    print(status)
    print("Digite uma letra: ")
    chosenLetter = input()

    if chosenLetter in realWord:
        print("Acertou!")
        print("essa é a", realWord.index(chosenLetter) + 1, "letra")
        rightGuessedLetters[realWord.index(chosenLetter)] = chosenLetter

    else:
        print("Errou!")
        wrongGuessedLetters.append(chosenLetter)
        print("Letras erradas: ", wrongGuessedLetters)

    if "_" not in rightGuessedLetters:
        print("Você ganhou!")
        print("A palavra é", realWord)
        print("gosta de jogar de novo? (s/n)")
        playAgain = input()
        if playAgain == "s":
            firstRound = True
        elif playAgain == "n":
            programWorking = False

    if len(wrongGuessedLetters) == 6:
        print("Você perdeu!")
        print("gosta de jogar de novo? (s/n)")
        playAgain = input()
        if playAgain == "s":
            firstRound = True
        elif playAgain == "n":
            programWorking = False
