from user import User

users = [User(1,"Sai","Saipass"),
         User(2,"Meghna","Meghnapass")]

username_table={u.username:u for u in users}
userid_table={u.id:u for u in users}

def authenticate(usern,passw):

    user=username_table.get(usern,None)

    if user and passw==user.password:
        return user