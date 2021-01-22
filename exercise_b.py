import math

class LocationError(Exception):
    """Raised if input values are incorrect"""
    pass

class Location:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


    def distance(self, other):
        r = 6373.0

        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.radians(other.latitude)
        lon2 = math.radians(other.longitude)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return math.ceil(r * c)

    def check(self, long):
        x = float(self, long)

        if x[0] < -90:
            raise LocationError("Latitude value is under -90")
        elif x[0] > 90:
            raise LocationError("Latitude value is above 90")
        elif [1] < -180:
            raise LocationError("Longitude value is under -180")
        elif [1] > 180:
            raise LocationError("Longitude value is above 180")
        else:
            return x





