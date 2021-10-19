from core_classes import person as p


def create_person():
    print("Enter first name: ")
    f_name = input()
    print("Enter last name: ")
    l_name = input()
    print("Enter age: ")
    age = int(input())
    print("Enter gender (M - male or F - female): ")
    gender = input()
    print("Enter id number: ")
    id_number = int(input())

    if gender == 'm' or gender == 'M':
        gender = 'Male'
    else:
        gender = 'Female'

    p.Person(f_name, l_name, gender, age, id_number)
    p.Person.save_to_file()


if __name__ == '__main__':
    create_person()
    print(f'\n Person Created: {p.Person.people}')
