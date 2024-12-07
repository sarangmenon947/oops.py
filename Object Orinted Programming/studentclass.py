class Student:
    name = ""
    age = 14
    class_teacher = "Poonam"

    def __init__(self):
        print("We Are Creating A New Student")

    def change_details(self):
        print("Please Enter Your Age ")
        self.age = input()
        print("Please Enter Your Name ")
        self.name = input()

    def show_details(self):
        print("The Details Of The Students Are: ")
        print(self.name, self.age, self.class_teacher)

sarang = Student()
sarang.change_details()
sarang.show_details()