def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a = 2, b='дерево', c = 3)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list=[4,5,6]
values_dict={'a':3,'b': 15, 'c':7}
print_params(*values_list)
print_params(**values_dict)

values_list_2=[4.5,'кино']
print_params(*values_list_2, 42)




