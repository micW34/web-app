from fastapi import FastAPI, Depends
from .services.holiday_service import HolidayService  # import class (service) w/ greeting method
from .services.xmas_service import XmasService

api = FastAPI()

@api.get("/")
def hello(holiday_service = Depends(HolidayService)):
    return holiday_service.get_hello("Micah")

@api.get("/")
def xmas(xmas_service = Depends(XmasService)):
    return xmas_service.days_until()