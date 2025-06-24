from data_class import User

class NoneUserClassError:
    '''döndürülen değer bir User nesnesi değilde None ise bu hata fırlatılır.'''

class UserClass:
    def __init__(self):
        self.users: list[User] = []

    def add(self, user: User)-> None:
        self.users.append(user)

    def get_user(self, id:int) -> User | None:
        return next((u for u in self.users if u.user_id == id),None)
    

def main():
    user1 = User("umut", 20, "umut@gmail.com",active=True)
    user2 = User("okan", 20, "okan@gmail.com",active=False)
    mng = UserClass()
    mng.add(user1)
    mng.add(user2)

    print("--- Liste ---")
    for u in mng.users:
        print(u)


if __name__ == "__main__":
    main()