import os

DATA_FILE = "atm_users.txt"


class User:
    """Represents a single ATM user."""
    def __init__(self, pin, balance=0.0, name="Unknown"):
        self.pin = pin
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount >= self.balance:
            return False
        self.balance -= amount
        return True

    def to_text(self):
        return f"{self.pin},{self.balance},{self.name}"

    @staticmethod
    def from_text(line):
        try:
            pin, balance, name = line.strip().split(",")
            return User(pin, float(balance), name)
        except:
            return None


class ATM:
    """ATM system that manages multiple users."""
    def __init__(self):
        self.users = {}
        self.load_users()

# ---------------- User Management ---------------- #

    def load_users(self):
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r",encoding='utf-8') as file:
            for line in file:
                user = User.from_text(line)
                if user:
                    self.users[user.pin] = user

    def save_users(self):
        with open(DATA_FILE, "w",encoding='utf-8') as file:
            for user in self.users.values():
                file.write(user.to_text() + "\n")

    def register_user(self):
        print("\n--- Register New User ---")
        name = input("Enter your name: ")

        # PIN creation
        while True:
            pin = input("Create PIN (4 digits): ")
            if pin.isdigit() and len(pin) == 4:
                if pin not in self.users:
                    break
                else:
                    print("This PIN already exists! Choose another.")
            else:
                print("PIN must be exactly 4 digits!")

        # add firs balance
        while True:
            try:
                balance = float(input("Enter starting balance: "))
                break
            except ValueError:
                print("Invalid number!")

        new_user = User(pin, balance, name)
        self.users[pin] = new_user
        self.save_users()

        print("User registered successfully!\n")

    def login(self):
        print("\n--- ATM Login ---")
        pin = input("Enter your PIN: ")

        if pin in self.users:
            print(f"Welcome, {self.users[pin].name}!\n")
            return self.users[pin]
        else:
            print("Invalid PIN!\n")
            return None

# ---------------- ATM Operations ---------------- #

    def check_balance(self, user):
        print(f"Your balance is: {user.balance}₾\n")

    def deposit_money(self, user):
        try:
            amount = float(input("Enter amount to deposit: "))
            if user.deposit(amount):
                print("Deposit successful!\n")
            else:
                print("Invalid amount!\n")
        except ValueError:
            print("Invalid input!\n")

    def withdraw_money(self, user):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if user.withdraw(amount):
                print("Withdrawal successful!\n")
            else:
                print("Not enough balance or invalid amount!\n")
        except ValueError:
            print("Invalid input!\n")

    # ---------------- Main Menu ---------------- #

    def main_menu(self):
        while True:
            print("---------- ATM SYSTEM ----------")
            print("1. Register New User")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.register_user()

            elif choice == "2":
                user = self.login()
                if user:
                    self.user_menu(user)

            elif choice == "3":
                self.save_users()
                print("Goodbye!")
                break
            else:
                print("Invalid option!\n")

    def user_menu(self, user):
        while True:
            print("------ ATM Operations ------")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Log Out")

            choice = input("Choose option: ")

            if choice == "1":
                self.check_balance(user)
            elif choice == "2":
                self.deposit_money(user)
                self.save_users()
            elif choice == "3":
                self.withdraw_money(user)
                self.save_users()
            elif choice == "4":
                print("Logging out...\n")
                break
            else:
                print("Invalid option!\n")


# Run ATM
atm = ATM()
atm.main_menu()
