from ninja import NinjaAPI
from departments.views import router as departments_router

api = NinjaAPI()


api.add_router("departments", departments_router, tags=["Departments"])
