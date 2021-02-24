s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')  # find ищет первое вхождение слова по индексу всей строки
if index != -1:
    print(f'Substring found at index {index}')