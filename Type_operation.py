import copy

# list - changable type of data
simple_list = [1, 2, 3, 4, 5, 6]
print(simple_list, id(simple_list))
print("------------------------------------")
simple_list = simple_list[::-1]
print(simple_list, id(simple_list))
print("------------------------------------")
copy_list = simple_list.copy()
print(copy_list, id(copy_list))
print("------------------------------------")
deep_copy_list = copy.deepcopy(simple_list)
print(deep_copy_list, id(deep_copy_list))
print("------------------------------------")
simple_list[0], simple_list[1] = simple_list[1], simple_list[0]
print(simple_list, id(simple_list))
print("------------------------------------")

# dict - changable type of data
a = {
    1: "aaaa",
    2: "bbbb",
    3: "cccc"
}
print(a, id(a))
a[1] = "eeee"
print(a, id(a))
print("------------------------------------")

# set - changable type of data
a = {
    1, 2, 3, 4, 5
}
print(a, id(a))
a = {6, 7, 8}
print(a, id(a))
print("------------------------------------")

# int, float, decimal, bool, str, tuple, range, frozenset - not changable types of data
int
digit = 9
print(digit, id(digit))
digit = 11
print(digit, id(digit))
print("------------------------------------")

# str
digit = "fduhfdh554fdf"
print(digit, id(digit))
digit = "858548548aksam"
print(digit, id(digit))
print("------------------------------------")
tuple
tup = (1, 2, 3)
print(tup, id(tup))
tup = (4, 5, 6)
print(tup, id(tup))
print("------------------------------------")
