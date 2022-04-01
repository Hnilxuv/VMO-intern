from bank_manage import manage_saving_accounts
from bank_manage import manage_checking_accounts
from bank_manage import customer_manage
from bank_manage import  customer

#khoi tao doi tuong quan ly
listSA = manage_saving_accounts()
listCA = manage_checking_accounts()
listC = customer_manage()

while (1 == 1):
    print("\nBanking Management")
    print("*************************MENU**************************")
    print("**  1. Add Customer.                                 **")
    print("**  2. Show Customer List                            **")
    print("**  0. Exit.                                         **")
    key = int(input("Enter choose: "))

    if (key == 1):
        print("\n1. Add Customer.")
        listC.addCustomer()
        print("\nDone!")
    elif(key == 2):
        print("\n2. Show Customer List.")
        listC.showCustomerList(listC.getCustomerList())
        id = int(input("Enter id: "))
        c: customer = listC.findByID(id)
        if(c != None):
            print("1. Add Saving Account.")
            print("2. Add Checking Account.")
            print("3. Show Account List.")
            print("0. Back")
            while 1 == 1:
                key = int(input("Enter choose: "))
                if key == 1:
                    print("1. Add Saving Account.")
                    listSA.addSavingAccount(id)
                elif key == 2:
                    print("2. Add Checking Account.")
                    listCA.addCheckingAccount(id)
                elif key == 3:
                    print("3. Show Account List.")
                    print("\n")
                    sa = len(listSA.findByID(id))
                    ca = len(listCA.findByID(id))
                    print("Total number of accounts",ca + sa )
                    print("1.Saving Account:", sa)
                    print("2.Checking Account:", ca )
                    print("0. Back")
                    while 1 == 1:
                        key = int(input("Enter choose: "))
                        if key == 1:
                            print("1.Saving Account:")
                            listSA.showSavingAccount(listSA.findByID(id))
                        elif key == 2:
                            print("2.Checking Account:")
                            listCA.showSavingAccount(listCA.findByID(id))
                        elif key == 0:
                            print("\nBack")
                            break
                        else:
                            print("\nError choose!")
                            print("\nAgain Choose")

                elif key == 0:
                    print("\nBack")
                    break
                else:
                    print("\nError choose!")
                    print("\nAgain Choose")
        else:
            print("Customer does not exist")

