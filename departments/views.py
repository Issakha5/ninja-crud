from http import HTTPStatus
from typing import List

from django.http import HttpRequest
from ninja import Router
from ninja.pagination import LimitOffsetPagination, paginate

from departments.models import Department
from departments.schemas import DepartmentIn, DepartmentOut

router = Router()


@router.get("/", response={HTTPStatus.OK: List[DepartmentOut]})
@paginate(LimitOffsetPagination)
def list_departments(request: HttpRequest):
    return Department.objects.all()


@router.post("/", response={HTTPStatus.CREATED: DepartmentOut})
def create_department(request: HttpRequest, payload: DepartmentIn):
    department = Department(**payload.dict())
    department.full_clean()
    department.save()
    return HTTPStatus.CREATED, department


@router.get("/{id}", response={HTTPStatus.OK: DepartmentOut})
def retrieve_department(request: HttpRequest, id: int):
    department = Department.objects.get(id=id)
    return department


@router.put("/{id}", response={HTTPStatus.OK: DepartmentOut})
def update_department(request: HttpRequest, id: int, payload: DepartmentIn):
    department = Department.objects.get(id=id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(department, attr, value)
    department.full_clean()
    department.save()
    return department


@router.delete("/{id}", response={HTTPStatus.NO_CONTENT: None})
def delete_department(request: HttpRequest, id: int):
    department = Department.objects.get(id=id)
    department.delete()
    return HTTPStatus.NO_CONTENT, None
