from sale_manage import product_manage
from sale_manage import customer_manage
from sale_manage import  bill_manage
from sale_manage import  billdetail_manage

listProduct = product_manage()
listCustomer = customer_manage()
listBill = bill_manage()
listBillDetail = billdetail_manage()

while (1 == 1):
    print("\nSale Management")
    print("*************************MENU**************************")
    print("**  1. Add Product.                                  **")
    print("**  2. Add Customer.                                 **")
    print("**  3. Create Bill.                                  **")
    print("**  4. Show Bill List.                               **")
    print("**  5. Show Customer Lists                           **")
    print("**  0. Exit.                                         **")
    key = int(input("Enter choose: "))
    if (key == 1):
        print("\n1. Add Product.")
        f = open("products.txt", "w")
        f.write("{:<8} {:<18} {:<15} {:<15} {:<15}".format("id", "Product Name", "Category", "Brand", "Price"))
        f.write("%s\n" % "")
        f.close()
        listProduct.inputProduct()
        print("\nDone!")
    elif (key == 2):
        print("\n2. Add Customer.")
        f1 = open("customer.txt", "w")
        f1.write("{:<10} {:<18} {:<8}".format("id", "Customer Name", "Phone"))
        f1.write("%s\n" % "")
        f1.close()
        listCustomer.inputCustomer()
        print("\nDone!")
    elif (key == 3):
        print("\n3. Create Bill.")
        print("\nEnter Bill Infor.")
        listBill.inputBill()
        listProduct.showListProduct(listProduct.getlistProduct())
        print("1.Add Bill Detail.   ")
        print("2.Exit               ")
        while(1 == 1):
            key1 = int(input("Enter choose: "))
            if(key1==1):
                print("\nEnter Bill Detail.")
                listBillDetail.inputBillDetail()
            elif(key1 == 2):
                print("\nDone")
                break
    elif (key == 4):
        listBill.showListBill(listBill.getlistBill())
        id = input("enter Bill ID to show bill detail: ")
        rs = listBillDetail.findByID(id)
        listBillDetail.showListBillDetail(rs)

    elif(key == 5):
        listCustomer.showListCustomer(listCustomer.getlistCustomer())
        customerID = input("enter Customer ID: ")
        rs = listBill.findByID(customerID)
        listBill.showListBill(rs)
        billID = input("enter Bill ID to show bill detail: ")
        rs2 = listBillDetail.findByID(billID)
        listBillDetail.showListBillDetail(rs2)
    elif key == 0:
        print("\nExit")
        break
    else:
        print("\nError choose!")
        print("\nEnter choose.")

