#ScarletPrescott
class User():
    """Simple user profile"""
    def __init__(self, first_name, last_name, age, username, favorite_color):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.username = username
        self.favorite_color = favorite_color
        self.login_attempts = 0

    def describe_user(self):
        print(f"The User Details are Below:")
        print("First Name:", self.f_name)
        print("Last Name:", self.l_name)
        print("Age:", self.age)
        print("Username:", self.username)
        print("Favorite Color:", self.favorite_color)

    def greet_user(self):
        print(f"Hello, {self.username.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
