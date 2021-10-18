import person as p


class Admin(p.Person):
    login_details = {}

    def __init__(self, first_name: str, last_name: str, gender: str, admin_username: str, admin_pin: int, age: int = 0,
                 id_number: int = 0):
        super().__init__(first_name, last_name, gender, age, id_number)

        self.admin_username = admin_username
        self.admin_pin = admin_pin

    def admin_login_details(self):
        pass
