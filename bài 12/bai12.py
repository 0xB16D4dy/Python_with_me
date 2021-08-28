from os import write


with open('input.inp', 'r', encoding='utf-8') as input:
    word = input.readlines()
    string = ''.join(word).replace('\n','')
with open('output.out', 'a') as output:
    output.write(string)