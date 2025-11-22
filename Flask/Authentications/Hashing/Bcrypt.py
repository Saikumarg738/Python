from argon2 import hash_password
from flask_bcrypt import Bcrypt

passw="root1234"

bcobj=Bcrypt()

hashpass=bcobj.generate_password_hash(password=passw)

print(hashpass)

if(bcobj.check_password_hash(hashpass,'root1234')):
    print("Correct password")
else:
    print("Incorrect password")