#-*-coding:utf8;-*-

#lista = ['Λ','ß','↻','Ð','☰','∲','ç','╫','¡','¿','↑','ღ','∏','☐','þ','¶','┏','§','⊥','ü','y','₪','x','¥','³|']

lista = []

palavra = input('Palavra: ')

num = len(palavra)

for num in range(0, num):
    if palavra[num] == 'Λ':
        lista.append('A')
    elif palavra[num] == 'ß':
        lista.append('B')
    elif palavra[num] == '↻':
        lista.append('C')
    elif palavra[num] == 'Ð':
        lista.append('D')
    elif palavra[num] == '☰':
        lista.append('E')
    elif palavra[num] == '∲':
        lista.append('F')
    elif palavra[num] == 'ç':
        lista.append('G')
    elif palavra[num] == '╫':
        lista.append('H')
    elif palavra[num] == '¡':
        lista.append('I')
    elif palavra[num] == '¿':
        lista.append('J')
    elif palavra[num] == '├':
        lista.append('K')
    elif palavra[num] == '↑':
        lista.append('L')
    elif palavra[num] == 'ღ':
        lista.append('M')
    elif palavra[num] == '∏':
        lista.append('N')
    elif palavra[num] == '☐':
        lista.append('O')
    elif palavra[num] == 'þ':
        lista.append('P')
    elif palavra[num] == '¶':
        lista.append('Q')
    elif palavra[num] == '┏':
        lista.append('R')
    elif palavra[num] == '§':
        lista.append('S')
    elif palavra[num] == '⊥':
        lista.append('T')
    elif palavra[num] == 'ü':
        lista.append('U')
    elif palavra[num] == 'y':
        lista.append('V')
    elif palavra[num] == '₪':
        lista.append('W')
    elif palavra[num] == '✕':
        lista.append('X')
    elif palavra[num] == '¥':
        lista.append('Y')
    elif palavra[num] == ' ':
        lista.append(' ')
    else:
        lista.append('Z')
t = len(lista)
for i in range(0, t):
    print (lista[i])
