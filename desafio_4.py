with open("desafio_4.txt", "r") as arquivo:
	cifras = arquivo.read()

#PARA SEPARA AS LINHAS
cifras = cifras.split('\n')

#FUNÇÕES DO DESAFIO 3
def xor(encoded, chave):
    exec_xor = [i ^ chave for i in encoded]
    return bytes(exec_xor)

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

def des_hex(hex_string):
    traduzido = bytes()
    for i in range(0, len(hex_string), 2):
        traduzido += bytes([int(hex_string[i:i+2], 16)])
    return traduzido

cifras = list(map(des_hex, cifras))
possiveis_letras = []

for i in cifras:
    for chave in range(255):
        letra = xor(i, chave)
        possiveis_letras.append(letra)

print(max(possiveis_letras, key=letras))

