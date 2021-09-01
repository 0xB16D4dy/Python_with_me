# with open('input.inp', 'r', encoding='utf-8') as input:
#     word = input.readlines()
#     string = ''.join(word).replace('\n','')
# with open('output.out', 'a') as output:
#     output.write(string)

#bài 13 

try:
    with open('input.inp', 'r', encoding='utf-8') as inp:
        word = inp.readlines()
        string = ''.join(word).replace('\n', '')
    with open('output.out', 'w') as out:
        out.write(string)
except FileNotFoundError:
    with open('output.out', 'a') as out:
        out.write('không tìm thấy file')
