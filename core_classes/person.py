import os


class Person:
    people = []

    def __init__(self, first_name: str, last_name: str, gender: str, age: int = 0, id_number: int = 0):
        assert age >= 0, f"Age {age} should be greater or equal to 0"

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.id_number = id_number

        Person.people.append(self)

    def __repr__(self):
        return f"Person('{self.first_name}', '{self.last_name}', '{self.gender}', {self.age}, {self.id_number})"

    @staticmethod
    def save_to_file():

        if not os.path.isfile('people.txt'):
            file = open('people.txt', 'a')
            file.writelines('First_Name \t\t' + 'Last_Name \t\t' + 'Age \t\t' + 'Gender \t\t' + 'ID_Num \n')


            for person in Person.people:
                file.write(person.first_name + '\t\t\t')
                file.write(person.last_name + '\t\t\t')
                file.write(str(person.age) + '\t\t\t')
                file.write(person.gender + '\t\t')
                file.write(str(person.id_number))
                file.write('\n')

            file.close()

        else:
            file = open('people.txt', 'a')

            for person in Person.people:
                file.write(person.first_name + '\t\t\t')
                file.write(person.last_name + '\t\t\t')
                file.write(str(person.age) + '\t\t\t')
                file.write(person.gender + '\t\t')
                file.write(str(person.id_number))
                file.write('\n')
            file.close()

    def display(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Id Number: {self.id_number}")
