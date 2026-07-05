def search(phonebook):
    name1 = input("Enter the name to search: ")
    if name1 in phonebook:
        print(f'number={phonebook[name1]}')
    else:
        print('name is not in phonebook.')

def add(phonebook):
    name1 = input("Enter the name: ")
    num = input("Enter the number: ")
    phonebook[name1] = num

def delete(phonebook):
    name1 = input("Enter the name to delete: ")
    if name1 in phonebook:
        del phonebook[name1]
        print(f'{name1} deleted.')
    else:
        print('name is not in phonebook.')

phonebook = {
    'dive': '999', 'asih': '909'
}

search(phonebook)
add(phonebook)
delete(phonebook)