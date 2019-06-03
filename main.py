#adds and removes objects from linear linked list
#Author: Grace-H
#Date: 02 June 2019

import LLL    #LLL class file

lll = LLL.LLL()
print("*note: commands do not have to be captialized")

go = True
while go:
    #get command
    command = input("'ADD' 'REMOVE' 'PRINT' or 'QUIT': ")
    command = command.upper()

    #ADD
    if command == "ADD":
        data = input("Enter data: ")
        lll.add(data)

    #REMOVE
    elif command == "REMOVE":
        data = input("Enter data: ")
        lll.remove(data)

    #PRINT
    elif command == "PRINT":
        print(lll)

    #QUIT
    elif command == "QUIT":
        go = False

    else:
        print("not an option")
