meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"una cara de risa",
            "CREEPY":"algo aterrador que da miedo",
            "BOOMER":"Persona que se aferra mucho al pasado",
            "PA":"para",
            "TROLLEAR": "hacer una broma"
            }
print(meme_dict)
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
print()
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Escribe otra palabra esa no existe")
