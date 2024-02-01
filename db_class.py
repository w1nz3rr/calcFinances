
import datetime


class User:
    id: int
    login: str
    password: str
    create_at: datetime.datetime
    update_at: datetime.datetime


class Category:
    id: int
    name: str
    description: str
    create_at: datetime.datetime
    update_at: datetime.datetime
    user_id: int
    color: str


class Operation:
    id: int
    type_operation: str
    date: datetime.datetime
    value: int
    description: str
    user_id: int
    category_id: int

