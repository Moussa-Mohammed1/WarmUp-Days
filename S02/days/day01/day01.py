def scope_test():
    test_var = "initial Value"
    def do_local():
        test_var = "local Value"
    def do_nonlocal():
        nonlocal test_var
        test_var = "nonlocal Value"
        
    def do_global():
        global test_var
        test_var = "global Value"

    do_local()
    print("\nAfter local assignement", test_var)

    do_nonlocal()
    print("\nAffter nonlocal assignement", test_var)
    
    do_global()
    print("\nAfter global assignement", test_var)

scope_test()
print("\nIn global scope:", test_var)

class Developer():
    company = "Company .co"
    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.skills = []
    def add_skill(self, skill):
        self.skills.append(skill)
        # print(f"{self.name} accomplished a new skill: {skill}")

dev1 = Developer("Alice", "python")
dev2 = Developer("Bob", "Java")

dev1.add_skill("Kanban")
from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
        self.__updated_at = None
        self.__created_at = datetime.now()
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        new_balance = self.deposit(interest)
        return new_balance

account = SavingsAccount('Moussa', 3999, 0.05)
account.apply_interest
