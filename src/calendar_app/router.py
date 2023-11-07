from fastapi import FastAPI, Depends
from .services.holiday_service import HolidayService  # import class (service) w/ greeting method

api = FastAPI()

@api.get("/")
def hello(holiday_service = Depends(HolidayService)):
    return holiday_service.get_hello("Micah")