from functions import create, remove, menu, show, update, update1
menu()
n = 1
while 5 > n > 0:
    n = int(input("\nUildliin dugaar oruulna uu: \n"))
    if n == 1:
        show()
    elif n ==2:
        create()
    elif n == 3:
        remove()
    elif n == 4:
        update1()
    else:
        print("Ta programmaas garlaa")