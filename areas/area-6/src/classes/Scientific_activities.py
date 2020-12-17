from ..classes.Users import User

class ScientificActivity:
    def __init__(self, id: int, name: str, users: list):
        self.s_activity_id = id
        self.name = name
        if not (
                isinstance(name, str) and
                isinstance(id, int)
        ):
            raise TypeError
        self.users = users

    def get_s_activity_id(self):
        return self.s_activity_id

    def get_name(self):
        return self.name

    def get_users(self):
        return self.users

    def set_s_activity_id(self, id: int):
        self.s_activity_id = id

    def set_name(self, name: str):
        self.name = name

    def set_users(self, users: list):
        self.users = users

    def add_user(self, user: User):
        self.users.append(user)
        return True

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__