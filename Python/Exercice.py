def longueur(contenu):
    long = 0
    for letter in contenu:
        long = long + 1
    return long


    long_phrase = longueur("j'aime les pizzas")
    long_phrase2 = longueur("ma phrase 2")
    print(long_phrase)
    print(long_phrase2)