def main() -> int:
    default_dict = dict() #default because no arguments
    print(default_dict)

    initialized_dict = dict([('name', 'Colton'), ('role', 'student')]) #easy for string arguments
    print(initialized_dict)

    simple_init_dict = dict(name = 'Colton', role = 'student') #can use if you don't necessarily want strings
    print(simple_init_dict)

    simple_init_dict['role'] = '27' #dictionaries are mutable
    print(simple_init_dict)

    my_comprehension = {x: x**2 for x in range(1,6)} #arbitrarily assign key value pairs (1,2,3,4,5)
    print(my_comprehension)

    my_comprehension = {x: x ** 2 for x in range(5)} #for index range up to but not including 5 (0-4)
    print(my_comprehension)

    s = "little,".translate({ord(i): None for i in string.punctuation})

    return 0