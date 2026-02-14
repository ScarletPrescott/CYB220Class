#ScarletPrescott
from user2 import User

class Admin(User):

    def __init__(self, first_name, last_name, age, username, favorite_color):
        super().__init__(first_name, last_name, age, username, favorite_color)

        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege.title()}")
        else:
            print("This user has no privileges")
