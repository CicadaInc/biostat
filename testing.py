with open('Base(test).txt', mode='r') as file:
    with open('Base(test)_1.txt', mode='w', encoding='utf-8') as file1:
        text = ''
        for line in file:
            line = line.replace(" ", "\t")
            text += line
        file1.write(text)
