import random as r
from datetime import datetime


# lop san pham
class Product:
    def __init__(self, productID, productName, category, brand, price):
        self.id = productID
        self.productName = productName
        self.category = category
        self.brand = brand
        self.price = price


# lop khach hang
class Customer:
    def __init__(self, customerID, customerName, phone):
        self.id = customerID
        self.name = customerName
        self.phone = phone


# cac ham quan li san pham
class product_manage:
    listProduct = []

    def generateID(self):
        maxId = 1
        if self.productAmount() > 0:
            maxId = self.listProduct[0].id
            for pr in self.listProduct:
                if maxId < pr.id:
                    maxId = pr.id
            maxId = maxId + 1
        return maxId

    def productAmount(self):
        return len(self.listProduct)

    def inputProduct(self):
        productID = self.generateID()
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        brand = input("Enter product brand: ")
        price = int(input("Enter product price: "))
        while price < 0:
            price = int(input("Enter product price: "))
        prd = Product(productID, name, category, brand, price)
        self.listProduct.append(prd)
        f = open('products.txt', 'a')
        for item in self.listProduct:
            f.write("{:<8} {:<18} {:<15} {:<15} {:<15}".format(item.id, item.productName, item.category, item.brand,
                                                               item.price))
            f.write("%s\n" % "")
        f.close()

    def showListProduct(self, listProduct):
        print("{:<15} {:<18} {:<10} {:<10} {:<10}".format("Product ID", "Name", "Catogory", "Brand", "Price"))
        for i in listProduct:
            print("{:<20} {:<18} {:<10} {:<10} {:<10}".format(i.id, i.productname, i.category, i.brand, i.price))
        print("\n")

    def getlistProduct(self):
        return self.listProduct


# ham sinh tu dong ma khach hang theo chuan UUID
def generateUUID():
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uuid_format = [3, 4]
    for n in uuid_format:
        for i in range(0, n):
            random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
        if n != 4:
            random_string += '-'
    return random_string


# cac ham quan ly khach hang
class customer_manage:
    listCustomer = []

    def inputCustomer(self):
        customerID = generateUUID()
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        cus = Customer(customerID, name, phone)
        self.listCustomer.append(cus)
        f = open('customer.txt', 'a')
        for item in self.listCustomer:
            f.write("{:<10} {:<18} {:<8} ".format(item.id, item.name, item.phone))
            f.write("%s\n" % "")
        f.close()

    def customerAmount(self):
        return len(self.listCustomer)

    def showListCustomer(self, listCustomer):
        print("{:<20} {:<18} {:<10} ".format("Customer ID", "Name", "Phone"))
        for i in listCustomer:
            print("{:<20} {:<18} {:<10}".format(i.id, i.name, i.phone))
        print("\n")

    def getlistCustomer(self):
        return self.listCustomer

    def findByID(self, ID):
        list = []
        if self.customerAmount() > 0:
            for i in self.listCustomer:
                if i.id == ID:
                    list.append(i)
        return list


# lop doi tuong hoa don
class bill:

    def __init__(self, billID, time, customerID, customerName):
        self.id = billID
        self.time = time
        self.customerID = customerID
        self.customerName = customerName


# lop doi tuong chi tiet hoa don
class billdetails:

    def __init__(self, billID, productID, quantity):
        self.billID = billID
        self.productID = productID
        self.quantity = quantity


class bill_manage:
    listBill = []

    def generateID(self):
        maxId = 1
        if self.billAmount() > 0:
            maxId = self.listBill[0].id
            for pr in self.listBill:
                if maxId < pr.id:
                    maxId = pr.id
            maxId = maxId + 1
        return maxId

    def billAmount(self):
        return len(self.listBill)

    def inputBill(self):
        billID = self.generateID()
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        customerID = input("Enter CustomerID: ")
        customerName = input("Enter CustomerName: ")
        b = bill(billID, time, customerID, customerName)
        self.listBill.append(b)

    def showListBill(self, listBill):
        print("{:<8} {:<20} {:<15} {:<8}"
              .format("ID", "Time", "Customer ID", "Customer Name", ))
        if len(listBill) > 0:
            for i in listBill:
                print("{:<8} {:<20} {:<15} {:<8}".format(i.id, i.time, i.customerID, i.customerName))
        print("\n")

    def findByID(self, ID):
        list = []
        if self.billAmount() > 0:
            for i in self.listBill:
                if i.customerID == ID:
                    list.append(i)
        return list

    def getlistBill(self):
        return self.listBill


class billdetail_manage:
    listBillDetail = []

    def inputBillDetail(self):
        billID = input("Enter BillID: ")
        customerID = input("Enter ProductID: ")
        quantity = int(input("Enter Product Quantity: "))
        billdt = billdetails(billID, customerID, quantity)
        self.listBillDetail.append(billdt)

    def billdetailAmount(self):
        return len(self.listBillDetail)

    def showListBillDetail(self, listBillDetail):
        print("{:<8} {:<20} {:<15} ".format("Bill ID", "Produce ID", "Quantity"))
        for i in listBillDetail:
            print("{:<8} {:<20} {:<15}".format(i.billID, i.productID, i.quantity))
        print("\n")

    def findByID(self, ID):
        list = []
        if self.billdetailAmount() > 0:
            for i in self.listBillDetail:
                if i.billID == ID:
                    list.append(i)
        return list
