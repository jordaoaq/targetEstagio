def contar_as(texto):

    texto_minusculo = texto.lower()
    quantidade_as = texto_minusculo.count('a')
    return quantidade_as

texto = input("Digite um texto: ")

quantidade = contar_as(texto)
print("A letra 'a' aparece", quantidade, "vezes no texto.")