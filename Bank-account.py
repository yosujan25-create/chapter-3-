class Account:
    def __init__(self, name, account_num, balance):
        self.name = name
        self._account_num = account_num
        self.__balance = balance

    # def display(self):
    #     print(f'Hi {self.name}, your account num is {self._account_num}, your current balance is {self.__balance}')

    def get_info(self):
        return self.__balance

    def seter_info(self, account, amount):
        if account == self._account_num and amount >= 50000:
            self.__balance = amount
            print(f"Welcome {self.name} your balance is {self.__balance}")
        else:
            print(f"You have insufficient balance {self.name} i.e {self.__balance}")


Account1 = Account("Sujan", 2023, 2700)

print(Account1.get_info())

Account1.seter_info(2023, 100000)
