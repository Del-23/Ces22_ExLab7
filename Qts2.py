from abc import ABC, abstractmethod
class Order(ABC): #Command
    def __init__(self, operations):
        self.operations = operations
    @abstractmethod
    def execute(self, **kwargs):
        pass
#-----------------------------------------------------------       
class Account():
    def __init__(self, id, money):
        self.id = id
        self.money = money
        self.counter = 0
        self.myTransfers = []
#-----------------------------------------------------------
class CheckBalance(Order): #ConcreteCommand
    def execute(self, **kwargs):
        self.operations.checkBalance(**kwargs)
    
class CheckExtract(Order): #ConcreteCommand
    def execute(self,  **kwargs):
        self.operations.checkExtract(**kwargs)

class Transfer(Order): #ConcreteCommand
    def execute(self,  **kwargs):
        self.operations.transfer(**kwargs)
#-----------------------------------------------------------
class Bank_operations: #Receiver
    def checkBalance(self, account):
        print (f"Your balance is {account.money}")
    def checkExtract(self, account):
        print (account.myTransfers)
        print (f"This account has done {account.counter} transfers")
    def transfer(self, account_origin, account_destiny, value):
        if account_origin.money >= value:
            account_origin.money -= value
            account_destiny.money += value
            account.myTransfers.append(value)
            print (f"You transfered {value}")
            account_origin.counter += 1
        else:
            print (f"You don't have enough money to transfer {value}")
#-----------------------------------------------------------
class Agent: #Invoker(chamador)
    def __init__(self):
        self.__order_queue = []
    def place_order(self, order, **kwargs):
        order.execute(**kwargs)  
#-----------------------------------------------------------
account = Account(1234, 1000)
account_destiny = Account(5678, 10000)

#Cliente
operations = Bank_operations()
checked_balance = CheckBalance(operations)
checked_extract = CheckExtract(operations)
value_to_transfer = Transfer(operations)

#Invoker
agent = Agent()
agent.place_order(checked_balance, account = account)
agent.place_order(checked_extract, account = account)
agent.place_order(value_to_transfer, account_origin = account, account_destiny = account_destiny, value = 500)
agent.place_order(value_to_transfer, account_origin = account, account_destiny = account_destiny, value = 100)
agent.place_order(checked_balance, account = account)
agent.place_order(checked_extract, account = account)


