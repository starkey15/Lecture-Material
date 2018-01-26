from csc131 import dictionaries

def main():
    print("Main")
    d = dictionaries.get_personal_data()
    for key in sorted(d.keys()):
        print("%s: %s" % (key,d[key]))



if __name__ == '__main__':
    main()