import math

class LocationError(Exception):
    """Raised if input values are incorrect"""
    pass

class Location:

    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

        self.check()


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

    def check(self):

        if self.latitude < -90 or self.latitude > 90:
            raise LocationError("Latitude value is under -90")
        
        if self.longitude < -180 or self.latitude > 180:
            raise LocationError("Latitude value is under -90")
        
        

if __name__ == '__main__':
    location1 = Location(51.514244, 7.468429)
    location2 = Location(47.2692124, 11.4041024)

    print(location1.distance(location2))
