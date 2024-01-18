class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount > 0:
                self.balance += amount
                print(f"До вашого рахунку додано {amount} грн. Поточний баланс: {self.balance} грн.")
            else:
                raise ValueError("Сума для внесення повинна бути більше 0.")
        except ValueError as e:
            print(f"Помилка: {e}")

    def withdraw(self, amount):
        try:
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Ви зняли {amount} грн. Поточний баланс: {self.balance} грн.")
            elif amount <= 0:
                raise ValueError("Сума для зняття повинна бути більше 0.")
            else:
                raise ValueError("Недостатньо коштів на рахунку.")
        except ValueError as e:
            print(f"Помилка: {e}")

    def check_balance(self):
        print(f"Поточний баланс: {self.balance} грн.")

# Приклад використання
account = BankAccount()

account.deposit(1000)
account.check_balance()

account.withdraw(500)
account.check_balance()

account.withdraw(700)
account.withdraw(-100)