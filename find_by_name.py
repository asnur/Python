# Fungsi find_by_name
def find_by_name(name, data):
    result = ''
    if name in data:
        result = 'Nama ' + name + ' diTemukan'
    else:
        result = 'Nama Tidak Ada'
    return result


list_name = ['asnur', 'angga', 'fahmi',
             'anggi', 'zaid', 'ayyash', 'nana', 'witri']
print(find_by_name('dede', list_name))
