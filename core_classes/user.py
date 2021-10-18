import person as p


class User(p.Person):
    login_details = {}

    def __init__(self, first_name: str, last_name: str, gender: str, username, password, age: int = 0,
                 id_number: int = 0):
        super().__init__(first_name, last_name, gender, age, id_number)

        self.username = username
        self.password = password


    def user_login_details(self):
        pass
