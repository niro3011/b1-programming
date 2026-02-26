import json


class UserStore:

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        users = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        user = json.loads(line)
                        users.append(user)
        except FileNotFoundError:

            pass
        return users

    def save(self, users):
        with open(self.file_path, "w") as file:
            for user in users:
                file.write(json.dumps(user) + "\n")

    def find_by_id(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None  

    def update_user(self, user_id, updated_data):
        users = self.load()
        for i in range(len(users)):
            if users[i]["id"] == user_id:

                users[i]["name"] = updated_data.get("name", users[i]["name"])
                users[i]["email"] = updated_data.get("email", users[i]["email"])
                self.save(users)
                return True
        return False 

    def delete_user(self, user_id):
        users = self.load()
        neue_liste = []
        gefunden = False
        for user in users:
            if user["id"] == user_id:
                gefunden = True  
            else:
                neue_liste.append(user)
        if gefunden:
            self.save(neue_liste)
        return gefunden
