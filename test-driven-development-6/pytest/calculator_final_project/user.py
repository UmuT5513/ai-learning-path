class User:
    def __init__(self, name, role):
        self._name = name
        self._role = role

    @property
    def name(self):
        return self._name
    
    @property
    def role(self):
        return self._role