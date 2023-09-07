def replace_terrible(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    occurrences = text.count('terrible')

    replaced_text = ''
    count = 0
    index = 0
    while index < len(text):
        if text[index:index+8] == 'terrible':
            count += 1
            if count % 2 == 0:
                replaced_text += 'pathetic'
            else:
                replaced_text += 'marvellous'
            index += 8
        else:
            replaced_text += text[index]
            index += 1

    with open('result.txt', 'w') as file:
        file.write(replaced_text)

    return occurrences

file_path = 'file_to_read.txt'
occurrences = replace_terrible(file_path)
print(f'Total occurrences of "terrible": {occurrences}')