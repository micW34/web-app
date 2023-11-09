from datetime import date, timedelta

class XmasService:
    def days_until(self):
        '''Look up today's date and return number of days until Christmas.'''
        
        this_day = date.today()

        # If after Christmas in given year, set xmas value to next year's Christmas
        if this_day.month == 12 & this_day.day > 25:
            xmas = date(this_day.year + 1, 12, 25)
        
        # If it is Christmas or is before Christmas in given year, set xmas to this year's Christmas
        else:
            xmas = date(this_day.year, 12, 25)

        num_days = xmas - this_day
        num_days = num_days.days

        return f"There are {num_days} days until Christmas!"