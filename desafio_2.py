str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

output = ''.join(['%x' % (int(x, 16) ^ int(y, 16)) for (x, y) in zip(str1, str2)])

print(output)