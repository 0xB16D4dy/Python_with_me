with open('input.inp', 'r', encoding='utf-8') as input:
    word = input.readlines()
    string = ' '.join(word).replace('\n','')
    print(string)