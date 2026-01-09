class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self) -> str:
        return f"{super().introduce()} My student ID is {self.student_id}."


class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, I'm {self.age} years old and I teach {self.subject}."


if __name__ == "__main__":
    s = Student("Alice", 20, "S12345")
    t = Teacher("Mr. Smith", 40, "Mathematics")

    print(s.introduce())
    print(t.introduce())


    print(isinstance(s, Person), isinstance(t, Person))