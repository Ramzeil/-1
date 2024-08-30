my_dict = {'Клава': 1987, "Вася": 1356, "Гера": 1818}
print('Dict:' , my_dict)
print('Existing value:' , my_dict ['Вася'])
print( 'Not existing value:' , my_dict.get("Зоя"))
print('Deleted value:', my_dict.pop('Гера'))
my_dict.update({'Роза': 1999, 'Марина' : 1988})
print('Deleted value:', my_dict.pop('Вася'))
print('Modified dictionary:' , my_dict)

my_set = {1, 3, "Яблоко", 3, 42.314, 'jack', 'sjoerd', 1 , 'jack'}
print('Set:' , my_set)
my_set.add(8)
my_set.add('Слон')
my_set.remove('Яблоко')
print("Modified set:" , my_set)