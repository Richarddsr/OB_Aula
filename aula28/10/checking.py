# checking accont class

# imports
from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number, account_dig, balance, agency, code):
        # super class
        super().__init__(agency, code)
        # private attributes
        self.__account_number = account_number
        self.__account_dig = account_dig
        self.__balance = balance

    # getters

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def account_dig(self):
        return self.__account_dig
    
    @property
    def balance(self):
        return self.__balance 
    
    # setters

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @account_dig.setter
    def account_dig(self, account_dig):
        self.__account_dig = account_dig

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # functions

    def __str__(self):
        return super().__str__() + (
            f"\nNumero da Conta:{self.__account_number}\n"
            f"Digito da Conta:{self.__account_dig}\n"
            f"Saldo:{self.__balance}\n"
        )
    
    def update_balance(self):
        self.__balance *= 1.01
        print("Saldo atualizado")
    
# instances
checking_account = CheckingAccount(12345, 6, 1000.0, "Banco do Brasil", 44998)
checking_account.update_balance()

# exit

print(checking_account)
        
   