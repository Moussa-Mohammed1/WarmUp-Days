# Function,Action,Input -> Output
# json.dumps(),Encode (Serialize),Python Object -> JSON String
# json.dump(),Encode (Serialize),Python Object -> JSON File
# json.loads(),Decode (Deserialize),JSON String -> Python Object
# json.load(),Decode (Deserialize),JSON File -> Python Object

import json

data = {'id': 1, 'name': 'Alice', 'is_active': True, 'roles': ['admin', 'user']}
json_string = json.dumps(data)
# print(json_string)
parsed = json.loads(json_string)
# print(parsed)

with open('S02/days/day02/data.json', 'w') as file:
    json.dump(data, file)
with open('S02/days/day02/data.json','r') as file:
    file_data = json.load(file)


# Custom serialization

class User:
    def __init__(self, username):
        self.username = username

def custom_encoder(obj):
    if isinstance(obj, User):
        return {"__type__": "User", "username" : obj.username}
    raise TypeError(f"Objet of type {type(obj).__name__} is not JSON serializable")

user = User("Moussa")

encoded_user = json.dumps(user, default=custom_encoder)
print(encoded_user)
# output {"__type__": "User", "username": "Moussa"}

#custom decoder 

def custom_decoder(dct):
    if dct.get("__type__") == "User":
        return User(dct["username"])
    return dct 

decoded_user = json.loads(encoded_user, object_hook=custom_decoder)
print(type(decoded_user))
#output: <class '__main__.User'>