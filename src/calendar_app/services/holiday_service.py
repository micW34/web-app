import requests
from datetime import date

class HolidayService:
    def __init__(self) -> None:
        self._api_key = "048ae5d9b643a363276fa02a39b77c6e2a7e1a49"
        self._api_link = "https://calendarific.com/api/v2/holidays"

    def get_today(self):
        '''Return US holidays for today.'''
        today = date.today()

        holidays = []

        request_parameters = {
            "api_key": self._api_key,
            "country": "US",
            "year": today.year,
            "month": today.month,
            "day": today.day,
        }
        json = requests.get(
            f"{self._api_link}", params=request_parameters
          ).json()
        response = json.get("response")
        json_holidays = response.get("holidays")

        for raw_holiday in json_holidays:
            holiday = {
                "name": raw_holiday.get("name"),
                "description": raw_holiday.get("description"),
                "date": raw_holiday.get("date").get("iso"),
            }
            holidays.append(holiday)
        return holidays

    def get_hello(self, name: str) -> str:
        '''Given a name, create and return a greeting.'''
        return f"Hello {name}"