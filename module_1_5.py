immutable_var = 1, 2, 'a', 'b'
print('immutable_var:', immutable_var)
print(immutable_var[0])
print(immutable_var[1])
#immutable_var=[1]=200
print('Кортеж относится к неизменяемым типам данных.')
print('Но в себе он может хранить изменяемые объекты, если внутри кортежа будет список.')
mutable_list=[1, 2, 3, 4, 'a','b']
print(mutable_list)
mutable_list[1]=17
mutable_list[2]='monkeys'
mutable_list[3]="elephant"
mutable_list[4]=99
print(mutable_list)
