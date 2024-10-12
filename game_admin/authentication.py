from hashlib import md5
import os

class User:
    def __init__(self):
        self.token1 = None
        self.token2 = None

    def login(self, username, password):
        if username == os.environ[
            "ADMIN_USERNAME"
        ] and password == os.environ["ADMIN_PASSWORD"]:           
            self.token1 = self.md5hash(username)
            self.token2 = self.md5hash(password)
            return True
        return False

    def is_authorized(self, token1, token2):
        if(token1 == self.md5hash(os.environ["ADMIN_USERNAME"]) and token2 == self.md5hash(os.environ["ADMIN_PASSWORD"])):
            return True
        return False
    
    # md5 hash algorithm
    def md5hash(self, raw):          
        hash_value = md5(raw.encode())
        final_value = hash_value.hexdigest()
        return final_value

    def get_token1(self):
        return self.token1
    
    def get_token2(self):
        return self.token2

   # Logout will be handled by the client, by removing the tokens from local storage or cookies

    def __str__(self):
        return f"User: {self.username}"
