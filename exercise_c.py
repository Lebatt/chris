from exercise_b import Location

#Muss ich immer einen neuen Exception error definieren? oder kann der aus exercise_b verwendet werden?
class InputError(Exception):
    """Raised if input values are incorrect"""
    pass

class Airport:

    def __init__(self, code, country, name, type, location):
        self.name = str(name)
        self.location = location

# 1) Wo müssen diese Statements hin?
# 2) Overriding methods: muss ich dafür für jeden member (code,country, etc.) zunächst eine Function erstellen, die dann was anderes returned?

        if len(code) == 4:
            self.code = code
        else:
            raise InputError("Code ist nicht valid ")

        if len(country) == 2:
            self.country = country
        else:
            raise InputError("country ist nicht valid")

        if type == "medium_airport" or type == "large_airport":
            self.type = type
        else:
            raise InputError("Type muss entweder medium_airport oder large_airport sein")

    def __str__(self): 
        return self.name

    def __sub__(self, other):
        return self.location.distance(other.location)

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)
