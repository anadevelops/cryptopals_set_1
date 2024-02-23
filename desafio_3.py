#O ALGORITMO DESSE DESAFIO FOI DESENVOLVIDO COM A AJUDA DE MUITOS VÍDEOS E PESQUISAS

#FUNÇÃO QUE EXECUTA O XOR
def xor(encoded, chave):
    exec_xor = [i ^ chave for i in encoded]
    return bytes(exec_xor)

#FUNÇÃO QUE CALCULA AS LETRAS MAIS COMUNS EM INGLÊS E VALIDA A EXISTÊNCIA NA LISTA DE PRINTABLES
def letras(frase):
    s = 0
    frase = frase.lower()
    dica = b"etaoin shrdlu"[::-1]

    for l in frase:
        if chr(l) in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c':
            i = dica.find(l)
            if i != -1:
                s += i
    return s

#FUNÇÃO QUE TRADUZ A STRING INICIAL DE HEX PARA BYTES
def des_hex(hex_string):
    traduzido = bytes()
    for i in range(0, len(hex_string), 2):
        traduzido += bytes([int(hex_string[i:i+2], 16)])
    return traduzido

encoded = des_hex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

chave = max(range(255), key=lambda x: letras(xor(encoded, x)))

descriptografado = xor(encoded, chave).decode('utf-8')

print(descriptografado)
print(chave)

