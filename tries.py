# Вместо счетной переменной в списке, получаем счетчик и значение из итерации
my_list = ['apple', 'pear', 'banana', 'apricot', 'grapes', 'peach']
for c, value in enumerate (my_list, 1):
    print (c, value)