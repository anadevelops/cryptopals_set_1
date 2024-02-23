#TRANSFORMEI A STRING COMO PEDIDO NO DESAFIO, MAS NÃO CONSEGUI CUMPRIR A EXIGÊNCIA DE SÓ USAR RAW BYTES
input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

hex_bin_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                  '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                  '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
                  'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111',
                  'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                  'E': '1110', 'F': '1111'}
base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

input_bin = ''.join(hex_bin_dict[i] for i in input)

for i in input_bin:
    if len(i) % 6 != 0:
        i = '0' + i

output = ''
for l in range(0, len(input_bin), 6):
    bit = input_bin[l:l+6]
    output += base64[int(bit, 2)]

print(output)