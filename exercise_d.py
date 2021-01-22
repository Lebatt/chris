from exercise_c import Airport, InputError
from exercise_b import Location, LocationError

class AirTrafficControl:
    """Dictionary: Airport Code = KEY"""
    dictionary = {}

    def new_airport(self):

        acode = input("Enter code: ")
        aname = input("Enter name: ")
        atype = input("Enter type: ")
        acountry = input("Enter country: ")
        alatitude = input("Enter latitude: ")
        alongitude = input("Enter longitude: ")

        try: 
            alocation = Location(alatitude, alongitude)
        except LocationError:
            self.new_airport()

        try:
            new_airport = Airport(acode, acountry, aname, atype, alocation)
            self.dictionary[new_airport.code] = new_airport
            print("// New Airport added")
            show_menu()
        except InputError:
            self.new_airport()

    def delete_airport(self, code): 
        del self.dictionary[code]
        print(self.dictionary)
        show_menu()

    def search_airport(self, code):
        if code in self.dictionary:
            print(self.dictionary[code]) # you can use print(Airport), beacause Airport overrides the method __str__
            return self.dictionary[code]
        else:
            print("\n// Airport not found")
            show_menu()

    def airport_list(self):
        print("------------ List of Airports -----------")
        for key in self.dictionary:
            print(self.dictionary[key])
        show_menu()
    
    def distance(self, codeA, codeB):
        try:
            a1 = self.search_airport(codeA)
            a2 = self.search_airport(codeB)

            print(a1.__sub__(a2))
        except:
            show_menu()


def show_menu():
    at = AirTrafficControl()

    print("\n-------------- Add new airport -----------")
    print("1- add airport")
    print("2- delete airport")
    print("3- search airport")
    print("4- calculate distance")
    print("5- Show list of airports")

    action = input("choose an action: ")

    if action == "1":
        at.new_airport()
    elif action == "2":
        code = input("Enter code of the airport: ")
        at.delete_airport(code)
    elif action == "3":
        code = input("Enter code of the airport: ")
        at.search_airport(code)
        show_menu()
    elif action == "4":
        codeA = input("Enter code of the first Airport: ")
        codeB = input("Enter code of the second Airport: ")
        at.distance(codeA, codeB)
    elif action == "5":
        at.airport_list()
    else:
        show_menu()
    

if __name__ == '__main__':
    show_menu()