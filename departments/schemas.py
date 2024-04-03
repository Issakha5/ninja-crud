from ninja import Schema


class DepartmentIn(Schema):
    title: str


class DepartmentOut(Schema):
    id: int
    title: str

