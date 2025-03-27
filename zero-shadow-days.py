import ephem
import math
from datetime import datetime, timedelta
from icecream import ic

def find_zero_shadow_days(latitude, year):
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.long = '0'  # Longitude doesn't affect zenith calculation
    observer.elevation = 0

    sun = ephem.Sun()
    zero_shadow_days = []

    # Iterate through each day of the year
    for day in range(1, 366):
        date = datetime(year, 1, 1) + timedelta(days=day - 1)
        observer.date = date.strftime('%Y/%m/%d %H:%M:%S')

        # Calculate the Sun's altitude at solar noon
        sun.compute(observer)
        altitude = math.degrees(sun.alt)
        ic(observer.date, altitude)

        # Check if the Sun is at zenith (altitude ~ 90 degrees)
        if abs(altitude - 90) < 0.1:  # Allow a small margin of error
            zero_shadow_days.append(date)

    return zero_shadow_days

# Example usage
latitude = 9.0  # Example latitude (Cairns, Australia)
year = 2025
zero_shadow_days = find_zero_shadow_days(latitude, year)
ic(zero_shadow_days)

print("Zero Shadow Days in", year, "for latitude", latitude, ":")
for date in zero_shadow_days:
    print(date.strftime('%Y-%m-%d'))
