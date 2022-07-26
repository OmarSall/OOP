class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):        #inheritance
    """This class generates checking account objects"""             #doc string
    type = "checking"           #class variable
   
    def __init__(self, filepath, fee):          #constructor - constructs the class
        Account.__init__(self, filepath)
        self.fee = fee


    def transfer(self, amount):     #method
        self.balance = self.balance - amount - self.fee         #instance variable

jacks_checking = Checking("account\\jack.txt", 1)      #object instance - instantiation of the class
jacks_checking.transfer(10)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)  #attributes


johns_checking = Checking("account\\john.txt", 1)      
johns_checking.transfer(10)
print(johns_checking.balance)
johns_checking.commit()

print(johns_checking.__doc__)           #doc string

#call an instance of a class - account variable (the object) that is created out of an object blueprint
# account = Account("balance.txt")
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.commit()