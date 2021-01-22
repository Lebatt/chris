import exercise_b
#Muss ich immer einen neuen Exception error definieren? oder kann der aus exercise_b verwendet werden?
class InputError(Exception):
    """Raised if input values are incorrect"""
    pass
class Airport:

    def __init__(self, code, country, name, type, location):
        self.name = str(name)
        self.location = exercise_b.Location(location)

# 1) Wo müssen diese Statements hin?
# 2) Overriding methods: muss ich dafür für jeden member (code,country, etc.) zunächst eine Function erstellen, die dann was anderes returned?

        if len(code) == 4:
            self.code = code
        else:
            raise InputError

        if len(country) == 2:
            self.country = country
        else:
            raise InputError

        if type == "medium_airport" or type == "large_airport":
            self.type = type
        else:
            raise InputError





