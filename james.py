print("sale tax")
Price = eval(input("enter purchase amount:"))
tax = Price * 0.06
sale = "{:.2f}".format (tax)
print("sale tax of", Price, "is", sale)