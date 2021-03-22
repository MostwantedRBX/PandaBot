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


def new_user(name,userid):
    create_user()
    with open("storage.json") as f:
        data = json.load(f)
    for user in data['users']:
        if user['name'] == "NameHere":
            user['name'] = name
        if user['id'] == 1234:
            user['id'] = userid
    write_json(data)

def get_points(userid):
    with open("storage.json") as f:
        data = json.load(f)
    for user in data['users']:
        if user['id'] == userid:
            return user['points']

def change_points(userid,value,way):
    with open("storage.json") as f:
        data = json.load(f)
    for user in data['users']:
        if user['id'] == userid:
            if way.lower() == "add":
                print("added")
                user['points'] = user['points'] + value
            elif way.lower() == "sub":
                print("taken")
                user['points'] = user['points'] - value
            break
    write_json(data)
    return True

    # for user in data["users"]:
    #     print(user['name'])
    #     if user['name'].lower() == "admin":
    #         user['points'] = user['points'] + 10




































# import boto3

# # Get the service resource.
# dynamodb = boto3.resource('dynamodb')
# # Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='users',
#     KeySchema=[
#         {
#             'AttributeName': 'username',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'last_name',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'username',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'last_name',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# # Wait until the table exists.
# table.meta.client.get_waiter('table_exists').wait(TableName='users')

# table.put_item(
#     Item={
#         'username': "mostwanted",
#         'points': 24123
#     }
# )

# table.get_item(

# )

# # Print out some data about the table.
# print(table.item_count)