import json

def beautify_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    with open(file_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def display_user_info(file_path):
    with open(file_path, 'r') as file:
        users = json.load(file)
        for user in users:
            print(f'{user["name"]}: {user["phoneNumber"]}')

beautify_json("ex_2.json")
display_user_info("ex_2.json")
