immutable_var = 1, "home", True, 0.5
print(immutable_var)
#immutable_var[0] = 111
#print(immutable_var)
#Не поддерживает обращение по элементам, но если засунуть в кортеж список то как мы уже знаем что списки изменяемы мы сможем его изменить
mutable_list = [1, "home", True, 0.5]
print(mutable_list)
mutable_list[0]= 2
mutable_list[1]= "street"
mutable_list[2]= False
print(mutable_list)