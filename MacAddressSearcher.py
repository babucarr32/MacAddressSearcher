from cProfile import run


def addMacAddress():
    print('\nAdd new MacAddress\n')
    macAddress = input("Enter MacAddress: ")
    name = input("Enter name: ")
    with open(r'MacAddress\macAddresses.txt', 'a') as f:
        newMAC = "\n" + macAddress + " 	" + name
        f.write(str(newMAC))
    f.close()
    

def main():
    found = False
    run = True
    with open(r'MacAddress\macAddresses.txt', 'r') as f:
            reader = f.readlines()
    
    while True:
        macAddress = input("Enter MacAddress: ")

        if macAddress == 'quit()':
            print('Closing...')
            quit()
        elif macAddress == 'add':
            addMacAddress()

        if len(macAddress) == 17:
            for i in reader:
                splitter = i.split()
                if macAddress == splitter[0]:
                    print('-'* 35)
                    print(i)
                    print('-'* 35)
                    found = True
                    break

            if found == False:
                print('-'* 45)
                print("MacAddress Unknown! ")
                print('-'* 45)
        else:
            pass
    
main()

    