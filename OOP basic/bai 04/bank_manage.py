#lop khach hang
class customer:
    def __init__(self, id, name ):
        self.id = id
        self.name = name

#lop tai khoan
class account_bank(customer):
    def __init__(self, id, name, account_number, balance):
        super().__init__(id,name)
        self.account_number = account_number
        self.balance = balance

#lop tai khoan tiet kiem
class Saving_Account(account_bank):
    def __init__(self, id, name, account_number, balance, bank_interest_rate, linkcode):
        super().__init__(id, name, account_number, balance)
        self.bir = bank_interest_rate
        self.linkcode = linkcode

    def getAccountNumber(self):
        return self.account_number

#lop tai khoan vang lai
class Checking_Account(account_bank):
    def __init__(self,id, name, account_number, balance,  linkcode):
        super().__init__(id, name, account_number, balance)
        self.linkcode = linkcode

    def getAccountNumber(self):
        return self.account_number

#quan ly khach hang
class customer_manage:
    #khoi tao danh sach khach hang
    listCustomer = []
    #khoi tao ma khach hang
    def generateID(self):
        maxId = 1
        if self.customerQuantity() > 0:
            maxId = self.listCustomer[0].id
            for pr in self.listCustomer:
                if maxId < pr.id:
                    maxId = pr.id
            maxId = maxId + 1
        return maxId

    def customerQuantity(self):
        return len(self.listCustomer)

    def addCustomer(self):
        #khoi tao khach hang moi
        id = self.generateID()
        name = input("Enter customer name: ")
        c = customer(id, name)
        self.listCustomer.append(c)


    def showCustomerList(self, listc):
        #hien thi danh sach khach hang
        print("{:<10} {:<25}  ".format("ID", "Customer Name" ))
        for i in listc:
            print("{:<10} {:<25} ".format(i.id, i.name))
        print("\n")

    def getCustomerList(self):
        return self.listCustomer

    #tim khach hang theo ma
    def findByID(self, id):
        rs = None
        for sa in self.listCustomer:
            if (sa.id == id):
                rs = sa
        return rs

class manage_saving_accounts:
    #khoi tao danh sach tai khoan tiet kiem
    listSavingAccount = []


    def addSavingAccount(self, id):
        #tao tai khoan tiet kiem
        Cid = id
        nameCustomer = customer_manage().findByID(id).name
        accountNumber = input("Enter account number: ")
        balance = int(input("Enter balance : "))
        bank_ir = balance*10/100
        linkcode = input("Enter account link code: ")
        sa = Saving_Account(Cid, nameCustomer, accountNumber, balance, bank_ir, linkcode)
        self.listSavingAccount.append(sa)

    #tim tai khoan tiet kiem theo id khach hang
    def findByID(self, id):
        listSA = []
        for sa in self.listSavingAccount:
            if (sa.id == id):
                listSA.append(sa)
        return listSA
    #hien thi danh sach tai khoan tiet kiem
    def showSavingAccount(self, listSA):
        print("{:<15} {:<20} {:<15} {:<15} {:<15} {:<15}".format("Customer Id", "Name", "Account Number", "Balance", "Bank IR", "Link Code"))
        for i in listSA:
            print("{:<15} {:<20} {:<15} {:<15} {:<15} {:<15}".format(i.id, i.name, i.account_number, i.balance, i.bir, i.linkcode))
        print("\n")

    def getListSA(self):
        return self.listSavingAccount

class manage_checking_accounts:
    listCheckingAccount = []

    def addCheckingAccount(self, id):
        Cid = id
        nameCustomer = customer_manage().findByID(id).name
        accountNumber = input("Enter account number: ")
        balance = int(input("Enter balance : "))
        linkcode = input("Enter account link code: ")
        ca = Checking_Account(Cid, nameCustomer, accountNumber, balance, linkcode)
        self.listCheckingAccount.append(ca)


    def findByID(self, id):
        listCA = []
        for ca in self.listCheckingAccount:
            if (ca.id == id):
                listCA.append(ca)
        return listCA

    def showSavingAccount(self, listCA):
        print("{:<15} {:<20} {:<15} {:<15} {:<15}".format("Customer Id","Name", "Account Number", "Balance", "Link Code"))
        for i in listCA:
            print("{:<20} {:<15} {:<15} {:<15} ".format(i.id, i.name, i.account_number, i.balance, i.linkcode))
        print("\n")

    def getListCA(self):
        return self.listCheckingAccount