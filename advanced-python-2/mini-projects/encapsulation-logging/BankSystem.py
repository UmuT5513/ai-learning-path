class PhoneLenError:
    '''telefon no uzunluğunu kontrol eder'''

class AmountError(Exception):
    def __init__(self, amount):
        if amount < 0:
            message = f"Amount cannot be negative: {amount}"
        else:
            message = f"Invalid amount: {amount}"
        super().__init__(message)


class BankAccount:
    
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
        self.__account_list = []

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def account_list(self):
        return self.__account_list
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value

    @classmethod
    def create_account(cls, data_str):
        balance, account_number = data_str.split(" ")
        bank_account = cls(balance, account_number)
        cls.account_list.append(bank_account)
        return bank_account
    
    def __str__(self):
        return f"account number: {self.__account_number}, balance: {self.__balance}"
    

class Person:
    def __init__(self, name, phone, job, accounts):
        self.__name = name
        self.__phone = phone
        self.__job = job
        self.accounts = accounts

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("string türünde bir değer girin")
        
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value):
        if isinstance(value, str):
            self.__phone = value
        else:
            raise TypeError
        
        if len(value) == 11:
            self.__phone = value
        else:
            print("telefon no 11 haneli olmalıdır!") 
            raise PhoneLenError
        
    @property
    def job(self):
        return self.__job
    
    def add_bank_account(self, account):
        '''account: BankAccount tipinde bir nesne'''
        self.accounts.append(account)

    def list_accounts(self):
        for i in self.accounts:
            print(f"account number: {i.account_number}\nbalance: {i.balance}")


class Management:
    customers = {} # key: person tipinde müşteri nesneleri, value: account tipinde hesap nesneleri
    def __init__(self, person, account):
        self.__person = person
        self.__account = account
        
    @property
    def person(self):
        return self.__person
    
    @property
    def account(self):
        return self.__account
    @classmethod
    def save_customers(cls):
        cls.customers[cls.person] = cls.account
        
    def select_account(self, account_number):
        account_number = input("hesap seçmek için ilgili hesabın hesap numarasını yazın: ")
        for i in self.person.accounts:
            if i.account_number == account_number:
                self.account = i

    def amount_validation(func):
        def wrapper(*args, **kwargs):
            import logging
            logging.basicConfig(
                    filename="bank.log",
                    encoding="utf-8",
                    filemode="a",
                    format="{asctime} - {levelname} - {message}",
                    style="{",
                    datefmt="%Y-%m-%d %H:%M",
                    level=logging.INFO,
                )
            try:
                func(*args, **kwargs)
            except AmountError:
                logging.warning(f"{func.__name__}, Girilen para değeri eksi bir değer olamaz!")
            else:
                logging.info(f"{func.__name__} işlemi basarili.")

            return func(*args, **kwargs)
        return wrapper
        
    @amount_validation
    def withdraw(self, amount):
        if amount<0:
            raise AmountError(amount)
        self.account.balance -= amount
        

    @amount_validation
    def deposit(self, amount):
        if amount<0:
            raise AmountError(amount)
        self.account.balance += amount

account1 = BankAccount(152000, 10011001)
account2 = BankAccount(50100, 10011002)
person = Person("umut", "1111111111", "çiftçi", accounts=[account1, account2])

generator = ((account for account in person.accounts))
for a in generator:
    print(a)

m1 = Management(person, account1)

m1.withdraw(-100)





