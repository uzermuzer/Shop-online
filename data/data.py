from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email:str = None
    telepfone: str = None
    password: str = None

