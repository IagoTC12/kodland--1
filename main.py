meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "Abreviação de verdade",
            "HATER": "Pessoa que critica as outras nas redes sociais",
            "VLW": "Abreviação de valeu",
            "POSTAR": "Publicar algo nas redes sociais"
            }



word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('essa palavra não existe')
