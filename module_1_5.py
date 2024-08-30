immutable_var = 1, 2, 'a', 'b'
print('immutable_var:', immutable_var)
mutable_list = [1, 2, 'a', 'b', 'Modified']
print('mutable_list:', mutable_list)
# Кортеж относится к неизменяемым типам данных.
mutable_list[1][2] = 200
print(mutable_list)
# Но в себе он может хранить изменяемые объекты, если внутри кортежа будет список.
