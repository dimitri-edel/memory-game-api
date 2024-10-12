from hashlib import md5
import os

class User:
    def __init__(self, usernameHash, passwordHash):
        self.usernameHash = usernameHash
        self.passwordHash = passwordHash
        self.authorized = False        

    def login(self):
        if self.usernameHash == self.md5hash(os.environ[
            "ADMIN_USERNAME"
        ]) and self.passwordHash == self.md5hash(os.environ["ADMIN_PASSWORD"]):
            self.authorized = True
            return True

    # md5 hash algorithm
    def md5hash(password):        
        hash_value = md5(password.encode())
        final_value = hash_value.hexdigest()
        return final_value   
        
    # logout
    def logout(self):
        self.authorized = False        

    def __str__(self):
        return f"User: {self.usernameHash}"
