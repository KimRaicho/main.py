class Person:
    people = []

    def __init__(self, first_name: str, last_name: str, gender: str, age: int = 0, id_number: int = 0):
        assert age >= 0, f"Age {age} should be greater or equal to 0"

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.id_number = id_number

        Person.people.append(self)

    @staticmethod
    def save_to_file():
        file = open('people.txt', 'a')
        file.writelines('First_Name \t' + 'Last_Name \t' + 'Age \t' + 'Gender \t' + 'ID_Num \n')

        for person in Person.people:
            file.write(person.first_name + '\t')
            file.write(person.last_name + '\t')
            file.write(str(person.age) + '\t')
            file.write(person.gender + '\t')
            file.write(str(person.id_number))
            file.write('\n')
        file.close()

    def display(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Id Number: {self.id_number}")
