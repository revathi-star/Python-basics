class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,deposit):
        self.balance+=deposit
    def withdraw(self,withdraw):
        self.balance-=withdraw
account=BankAccount(input())
for i in input():
    if i==2:
        for x in range(int(i)):
            if (input())[0]=='deposit':
                account.deposit((input())[1])
            if (input())[0]=='withdraw':
                account.withdraw((input())[1])
    if i==3:
        for x in range(int(i)):
            if (str(input(0)))[0]=='deposit':
                account.deposit((input())[1])
            if (input())[0]=='withdraw':
                account.withdraw((input())[1])

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        print(f'Product(name: {self.name}, price: {self.price}, quantity: {self.quantity})')
for i in range(3):
    l=input()
    v=l.split()
print(v)

