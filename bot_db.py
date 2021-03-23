import json

def write_json(data,filename='storage.json'):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)

def create_user():
    template_user = {
        "name": "NameHere",
        "id": 1234,
        "points": 100
    }

    with open("storage.json") as f:
        data = json.load(f)
        temp = data['users']
        temp.append(template_user)
        write_json(data)

def check_for_user(userid):
    with open("storage.json") as f:
        data = json.load(f)
        for user in data['users']:
            if user['id'] == userid:
                print('user found')
                return True
        return False

def new_user(name,userid):
    if check_for_user(userid) == False:
        create_user()
        with open("storage.json") as f:
            data = json.load(f)
        for user in data['users']:
            if user['name'] == "NameHere":
                user['name'] = name
            if user['id'] == 1234:
                user['id'] = userid
                write_json(data)
                return True   

def get_points(userid):
    with open("storage.json") as f:
        data = json.load(f)
    for user in data['users']:
        if user['id'] == userid:
            return user['points']

def change_points(userid,value,way):
    with open("storage.json") as f:
        data = json.load(f)
        print('loading data')
    for user in data['users']:
        if user['id'] == userid:
            print('user found')
            if way.lower() == "add":
                print("added")
                user['points'] = user['points'] + value
            elif way.lower() == "sub":
                print("taken")
                user['points'] = user['points'] - value
            break
    write_json(data)
    return True

