users = {
    "id" : 1,
    "name" : "leanne",
    "username" : "bret",
    "email" : "sincere@april.biz",
    "address" : {
        "street" : "kulas light",
        "suite" : "apt. 556",
        "city" : "gwenborough",
        "zipcode" : "92998-3874"
}
}
print(users)
print('\nChange to json')
import json
result = json.dumps(users)
print(type(result))

with open('result.json', 'w') as file :
    json.dump(users, file)
