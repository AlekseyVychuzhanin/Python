# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

text = ['hsdh', 'dhsd', 'df', 'dhsdh', 'df', 'dhmf', 'dfgjdfj']
search = 'df'
position = 2

def find_text(list, position):
    count = 0

    for i in range(0, len(text)):
        if search in text[i]:
            if count == position:
                return i
            else:
                count += 1
    if count < position:
        return -1

response = find_text(text, position)
print(response)
        