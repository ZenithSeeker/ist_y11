from typing import NamedTuple


class StudentRecord(NamedTuple):
    firstName : str
    surname : str
    age : int

def namedTuple1():
    student1 = StudentRecord("Bob", "Williamson", 19)

    print("Unformatted")
    print(student1)

    print("Sepereatly")
    print(student1.firstName)
    print(student1.surname)
    print(student1.age)
namedTuple1()