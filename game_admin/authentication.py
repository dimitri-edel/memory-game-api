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
            os.environ["ADMIN_TOKEN_1"] = self.generateToken()
            os.environ["ADMIN_TOKEN_2"] = self.generateToken()         
            self.token1 = os.environ["ADMIN_TOKEN_1"]
            self.token2 = os.environ["ADMIN_TOKEN_2"]            
            return True
        return False

    def is_authorized(self, token1, token2):
        if(token1 == os.environ["ADMIN_TOKEN_1"]) and token2 == os.environ["ADMIN_TOKEN_2"]:
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

    def generateToken(self):
        # generate a random string 20 characters long
        return os.urandom(20).hex()

    def __str__(self):
        return f"User: {self.username}"
