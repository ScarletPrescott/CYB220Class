#ScarletPrescott
from user import Admin

user0 = Admin("Sarah", "Grech", 34, "sgrech", "green")
user0.describe_user()

user0_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]

user0.privileges.privileges = user0_privileges

user0.privileges.show_privileges()
