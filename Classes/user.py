class User():
    """User profile class"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("First Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())

    def increment_login_attempts(self, logins):
        self.login_attempts =+ logins

    def reset_login_attempts(self):
        self.login_attempts = 0




sean = User('sean', 'gnanarajah')

sean.describe_user()

print(sean.login_attempts)

sean.increment_login_attempts(2)

print("You have attempted to login " + str(sean.login_attempts) + " times.")

sean.reset_login_attempts()

print('\n' + str(sean.login_attempts))