print('Question 15\n')

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount."

    def balanceNew(self):
        return f"Balance for {self.owner}: ${self.balance}"

account = BankAccount("John")
print(account.deposit(545))
print(account.withdraw(216))
print(account.balanceNew())

print('\nQuestion 16\n')

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return f"You borrowed '{self.title}'"
        return f"'{self.title}' is currently not available."

    def bookReturned(self):
        self.available = True
        return f"You returned '{self.title}'"

class Library:
    def __init__(self):
        self.books = []

    def bookAdded(self, book):
        self.books.append(book)

    def booksListed(self):
        return [f"{book.title} by {book.author} - {'Available' if book.available else 'Borrowed'}"
                for book in self.books]

book1 = Book("Lorax", "Dr. Seuss")
book2 = Book("Lord of the Rings: The Fellowship of the Ring", "J. R. R. Tolkien")
library = Library()
library.bookAdded(book1)
library.bookAdded(book2)

print(library.booksListed())
print(book1.borrow())
print(book2.borrow())
print(book1.bookReturned())
print(book2.borrow())
print(library.booksListed())


print('\nQuestion 17\n')

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def employeeDetails(self):
        return f"{self.name} - {self.department} - ${self.salary}"

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def employeeAdded(self, emp):
        self.employees.append(emp)

    def departmentDetails(self, department):
        return [emp.employeeDetails() for emp in self.employees if emp.department == department]

emp1 = Employee("James", "Civil Engineering", 75000)
emp2 = Employee("Arib", "Software Developer", 92000)
emp3 = Employee("Ronald", "Civil Engineering", 80000)
emp4 = Employee("Paul", "Psychologist", 60000)

manager = EmployeeManager()
manager.employeeAdded(emp1)
manager.employeeAdded(emp2)
manager.employeeAdded(emp3)
manager.employeeAdded(emp4)

print(manager.departmentDetails("Civil Engineering"))
print(manager.departmentDetails("Software Developer"))
print(manager.departmentDetails("Psychologist"))