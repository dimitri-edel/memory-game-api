from hashlib import md5
import os

class User:
    def __init__(self, username, passwordHash):
        self.username = username
        self.passwordHash = passwordHash
        self.authorized = False

    def login(self):
        if self.username == os.environ[
            "ADMIN_USERNAME"
        ] and self.passwordHash == self.hash_password(os.environ["ADMIN_PASSWORD"]):
            self.authorized = True
            return True

    # md5 hash algorithm
    def hash_password(password):
        print("md5 hash algorithm")
        hash_value = md5(password.encode())
        final_value = hash_value.hexdigest()
        return final_value

    def __str__(self):
        return f"User: {self.username}"
