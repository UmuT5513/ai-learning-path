from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Employee:
    first:str
    last:str
    pay:int
    # raise_amt: float = field(default=1.05) --> object variable
    raise_amt:ClassVar[float] = 1.05 #--> class variable

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        """
        Apply a pay raise to the employee.

        The pay is multiplied by the raise amount, which is
        initially set to 1.05 (5% increase). The new pay is
        rounded to the nearest integer and assigned back to
        the `pay` attribute.

        Returns None.
        """
        self.pay = int(self.pay * self.raise_amt)