from werkzeug.security import generate_password_hash,check_password_hash

passw="SaiKumar"

passhash=generate_password_hash(passw)

if(check_password_hash(passhash,"SaiKumar")):
    print("Correct pass")
else:
    print("Incorrect pass")

print(check_password_hash(passhash,"SaiKumar"))