class BankAccount:
    """Example class demonstrating various dunder methods"""

    def __init__(self, account_holder: str, balance: float) -> None:
        """__init__: Constructor - called when creating an instance"""
        self.account_holder = account_holder
        self.balance = balance
        print(f"Account created for {account_holder}")

    def __str__(self) -> str:
        """__str__: String representation for end users (print() friendly)"""
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    def __repr__(self) -> str:
        """__repr__: Official string representation for developers"""
        return f"BankAccount('{self.account_holder}', {self.balance})"

    def __add__(self, amount: float) -> "BankAccount":
        """__add__: Overload + operator (deposit money)"""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
        return self

    def __sub__(self, amount: float) -> "BankAccount":
        """__sub__: Overload - operator (withdraw money)"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds!")
        return self

    def __eq__(self, other: "BankAccount") -> bool:
        """__eq__: Overload == operator (compare balances)"""
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False

    def __lt__(self, other: "BankAccount") -> bool:
        """__lt__: Overload < operator (less than)"""
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return False

    def __le__(self, other: "BankAccount") -> bool:
        """__le__: Overload <= operator (less than or equal)"""
        if isinstance(other, BankAccount):
            return self.balance <= other.balance
        return False

    def __gt__(self, other: "BankAccount") -> bool:
        """__gt__: Overload > operator (greater than)"""
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        return False

    def __len__(self) -> int:
        """__len__: Allow len() to work on object (return balance as int)"""
        return int(self.balance)

    def __getitem__(self, key: str) -> any:
        """__getitem__: Allow indexing like account['holder'] or account['balance']"""
        if key == "holder":
            return self.account_holder
        elif key == "balance":
            return self.balance
        else:
            raise KeyError(f"Key '{key}' not found")

    def __call__(self) -> str:
        """__call__: Make the object callable like a function"""
        return f"Account summary: {self.account_holder} has ${self.balance:.2f}"

    def __del__(self) -> None:
        """__del__: Destructor - called when object is deleted"""
        print(f"Account for {self.account_holder} has been closed")


# Example usage
if __name__ == "__main__":
    # __init__: Creating instances
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 500)
    print()

    # __str__: Printing (user-friendly)
    print("Using __str__:")
    print(account1)
    print()

    # __repr__: Developer representation
    print("Using __repr__:")
    print(repr(account1))
    print()

    # __add__: Using + operator
    print("Using __add__ (+ operator):")
    account1 + 200
    print()

    # __sub__: Using - operator
    print("Using __sub__ (- operator):")
    account1 - 150
    print()

    # __eq__: Using == operator
    print("Using __eq__ (== operator):")
    print(f"account1 == account2: {account1 == account2}")
    print()

    # __lt__, __gt__: Using comparison operators
    print("Using __lt__ and __gt__ (comparison operators):")
    print(f"account1 > account2: {account1 > account2}")
    print(f"account1 < account2: {account1 < account2}")
    print()

    # __len__: Using len()
    print("Using __len__ (len() function):")
    print(f"len(account1): {len(account1)}")
    print()

    # __getitem__: Using indexing
    print("Using __getitem__ (indexing):")
    print(f"account1['holder']: {account1['holder']}")
    print(f"account1['balance']: {account1['balance']}")
    print()

    # __call__: Calling object as function
    print("Using __call__ (calling as function):")
    print(account1())
    print()

    # __del__: Object deletion
    print("Using __del__ (destructor):")
    del account2
