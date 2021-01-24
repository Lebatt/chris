from exercise_c import Airport, InputError
from exercise_b import Location, LocationError


class AirTrafficControl:
    """Dictionary: Airport Code = KEY"""
    dictionary = {}
#Exercise E:
    def file_import(filename):
        file = open(filename, 'r')
        for line in file:
            info = line.split(',')
            code = info[0]
            country = info[1]
            name = info[2]
            type = info[3]
            latitude = info[4]
            longitude = info[5]

        try:
            add_airport = Airport(code, country, name, type, Location(latitude, longitude))

            AirTrafficControl.dictionary[add_airport.code] = add_airport

        except LocationError(Exception):
            print("The information of the airport is not valid!")


        file.close()

#Exercise F
    def closest(given_location):
        the_list = []

        #iteration over entries in AirTrafficControl.dictionary
        for entry in AirTrafficControl.dictionary:
            #Distance calculation
            distance_calculation = AirTrafficControl.dictionary[entry].location.distance(given_location)
            #create tuple - first value distance between location AND instance of airport itself
            the_tuple = (distance_calculation, AirTrafficControl.dictionary[entry])
            #adding tuple to the list
            the_list.append(the_tuple)
        #sorting list by distance to location - https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
        sorted(the_list, key= lambda tupl: tupl[0])
        print(the_list[:10])


    def new_airport(self):

        acode = input("Enter code: ")
        aname = input("Enter name: ")
        atype = input("Enter type: ")
        acountry = input("Enter country: ")
        alatitude = input("Enter latitude: ")
        alongitude = input("Enter longitude: ")

        alocation = Location(alatitude, alongitude)
        try: 
            alocation = Location(alatitude, alongitude)
        except LocationError:
            self.new_airport()

        try:
            new_airport = Airport(acode, acountry, aname, atype, alocation)
            self.dictionary[new_airport.code] = new_airport
            print("\n New Airport added")
            show_menu()
        except InputError:
            self.new_airport()

    def delete_airport(self, code): 
        del self.dictionary[code]
        print(self.dictionary)
        show_menu()

    def search_airport(self, code):
        if code in self.dictionary:
            print(self.dictionary[code])  # you can use print(Airport), because Airport overrides the method __str__
            return self.dictionary[code]
        else:
            print("\n Airport not found")
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
            show_menu()
        except:
            show_menu()






def show_menu():
    at = AirTrafficControl()

    print("\n-------------- Airport Menu -----------")
    print("1- add airport")
    print("2- delete airport")
    print("3- search airport")
    print("4- calculate distance")
    print("5- show list of airports")

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

