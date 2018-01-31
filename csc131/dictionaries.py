def get_personal_data() -> dict:
    """
    :return: returns a dictionary of personal information.
    """
    personal_data = {"name": "Colton", "role": "student"}
    return personal_data

def main() -> int: #also found in 1-29-2018
    default_dict = dict() #default because no arguments
    print(default_dict)

    initialized_dict = dict([('name', 'Colton'), ('role', 'student')]) #easy for string arguments
    print(initialized_dict)

    simple_init_dict = dict(name = 'Colton', role = 'student') #can use if you don't necessarily want strings
    print(simple_init_dict)

    simple_init_dict['role'] = '27' #dictionaries are mutable
    print(simple_init_dict)

    my_comprehension = {x: x**2 for x in range(1,6)} #arbitrarily assign key value pairs (1-5)
    print(my_comprehension)

    my_comprehension = {x: x ** 2 for x in range(5)} #for index range up to but not including 5 (0-4)
    print(my_comprehension)

    s = "little,".translate({ord(i): None for i in string.punctuation}) #takes punctuation out of "s"
    print(s)

    return 0

import string
if __name__ == '__main__':
    main()