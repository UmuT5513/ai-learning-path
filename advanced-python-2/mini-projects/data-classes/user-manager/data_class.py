from dataclasses import dataclass, field

_next_id = 1 # sayaç

@dataclass
class User:
    name: str
    age:str
    email:str
    user_id:int = field(init=False, repr=False)
    active:bool = True


    def __post_init__(self):
        global _next_id
        self.user_id = _next_id
        _next_id += 1

        if "@" not in self.email:
            raise ValueError(f"Geçersiz e-posta: {self.email}")

    def __repr__(self):
        return f"UserId:{self.user_id} Email:{self.email} Active:{'✓'if self.active else '✗'}"