#lab02 reflection

""" #purely recursive solution, but not very efficient
    if (n == 2 or n == 1):
        return 1
    elif(n<1):
        return -1
    else:
        return fib(n-1) + fib(n-2)
"""

""" #approach 2
def main() -> int:
    my_dictionary = {}
    f = fib_memoization(20, my_dictionary)
    print(f)
    for key in sorted(my_dictionary.keys()):  #just prints in easy to read formatting
        print("%s: %s" % (key,my_dictionary[key])) #including optional

def fib_memoization(n: int, lookup: dict) -> int:         #memoization (top down approach)

    if n<1:
        return -1
    if n==1 or n==2:
        lookup[n] = 1
    if lookup.get(n,None) is None:        #only uses this function if n is not already found!
        lookup[n] = fib_memoization(n-1, lookup) + fib_memoization(n-2, lookup) #if value to n is not found, calculates
    return lookup[n]                                                            #and adds a value for it to lookup

if __name__ == '__main__':
    main()
"""

""" #approach 3
def fib_tab(n:int) -> int:     #using tabulation (bottom up)
    f = [0]*(n+1)              #opens array
    f[1] = 1                   #adds this value to array
    for i in range(2,n+1):     #start at two because f[1] is already defined
        f[i] = f[i-1] + f[i-2] #starts from the beginning and calculates up to n values
    return f[n]                #last value added to f is your answer
"""