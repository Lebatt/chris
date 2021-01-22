# Introduction to Programming Exercise 05

* Submission by Sunday (24-01-2021) 16:59:59 over OLAT https://lms.uibk.ac.at/olat/dmz/
* Compress your solution as tar.gz or zip file
* Do not forget to mark solved exercises
* Prepare your exercises so that you are able to present them during the course
* You might want to open this file in a program supporting markdown syntax or in 
  [gitlab](https://git.uibk.ac.at/c7031289/eidp_python)
* Code should be formatted as presented in the lecture slides (this includes naming conventions)

## Searching for Help

* You can always ask for help in the OLAT forum channel
* You can also contact me for questions by E-Mail [harald.schweiger@uibk.ac.at](mailto:harald.schweiger@uibk.ac.at)

## Tests and Documentation

Make sure that your solutions can be run with Python version 3.7 or higher.
Documenting your code is appreciated as it helps to understand the purpose of your code.
In case of faulty code good documentation can help in gathering points.


## Exercise A: Sorting with Lists (2 Points)

Create a function that returns a list of random numbers.
The size of the list should be passed as an argument.

Implement a function which takes a list as parameter and sorts it.
You are not allowed to use the sort method of lists or 
any sorting algorithm of another module. 
It is up to you which kind of sorting algorithm is implemented for this exercise.

Measure the time it takes for sorting lists of different sizes.
Show the average complexity of your algorithm by observing and comparing the size of the list with the resulting sorting time.

**_Hint_:** _You can use the class Stopwatch of slide 39 (lecture04) to measure the time._

**Submit as:** exercise_a.py


## Exercise B: Custom Exceptions (2 Points)

Extend the code of exercise_b with a custom exceptions class with the name `LocationError`.

Create a init method in class `Location` which takes as a parameter the latitude and longitude describing any position on the world.
* Check if the parameters are from type float.  
  If not try to convert them with `float(param)`.
* Check if the latitude is between -90 and 90 and if the longitude is between -180 and 180.  
  If not raise an exception of type `LocationError`.  
  Optionally pass a custom message to the constructor of the exception to clarify 
which of the two parameters is out of bounds or could not be converted.

If latitude and longitude are in a valid range assign them to a designated member variable.

Test if everything works correctly.
Check also if you can calculate the distance between two locations by the provided method.

**Submit as:** exercise_b.py


## Exercise C: Special Methods (2 Points)

Create a class `Airport` which stores the following parameters as members:
* **code:** a unique identification number of the airport consisting of 4 Letters
* **country:** a two letter [code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) 
               for the airport's country (AT, DE, IT)
* **name:** the name of the airport
* **type:** the type of the airport (medium_airport, large_airport)
* **location:** The location of the airport which should be of type `Location` as defined in `exercise_b`.

Overwrite the following methods with custom behavior:
* **\_\_str\_\_:** so that printing an airport just returns its name
* **\_\_sub\_\_:** returning the distance between two airports
* **\_\_hash\_\_:** to returns the hash of the airport code. `hash(self.code)`
* **\_\_eq\_\_:** to returns true if two airports have the same code.

Check if everything works as intended.
What happens if two Airports for which only the code is the same are added to a `set`.


**Submit as:** exercise_c.py

## Exercise D: Dictionaries (2 Points)

Create a class `AirTrafficControl` which manages a dictionary of Airports.
The key of the dictionary is the airport code and its values are instances of the class airport.

Implement a method with which a new airport can be created by reading some user input.
If the airport code has not 4 Letters or the country code 2 repeat the user input.
Also repeat the user input if an exception is thrown 
when for example an invalid location is passed to the constructor of the `Location` class.
If the input is successful add the airport to the dictionary.

Create a menu function outside the `AirTrafficControl` with which
* a new airport can be added.
* an airport can be deleted by its code.
* an airports can be searched by its code.
* the distance between two airports can be calculated.

Create all necessary methods inside the `AirTrafficControl` class and implement 
a nice user interface as seen in previous exercises. 

**Submit as:** exercise_d.py


## Exercise E: Reading a File (1 Point)

Extend `exercise_d` by implementing a method for the class `AirTrafficControl` with which 
a file can be read to add airports to the dictionary.
The method takes the filename as a parameter.

The file `medium_and_large_airports.csv` contains a list of medium and large airports of Germany, Austria and Italy.
Each line contains the airport information with the following order:  
```
code,country,name,type,latitude,longitude
```
As visible each airport attribute is separated by a comma.

**_Hint_:** _You can split a string using a comma as separator into a list of strings by using the string method 
[split](https://www.w3schools.com/python/ref_string_split.asp):_
```
info = line.split(',')
```

Inside the list is a airport with an invalid location.
Catch the `LocationError` that will be thrown as soon as the instance of the `Location` is created
and print the airport with the invalid location.
Do not add this airport to the dictionary and continue parsing the file till all airports have been added to the dictionary. 


## Exercise F: Sorting by List of tuples (1 Point)

Extend `exercise_d` by adding a menu option with which the 10 closet airports to a given location can be printed.
Therefore, implement a method inside `AirTrafficControl` which takes a location as parameter.
The method should return the 10 closest airports as list of tuples where the first value is the distance 
between the location passed as argument and the airport and the second value the instance of the airport itself.

The simplest way to achieve this behavior is iterating over all values/airports of the dictionary and adding
the distance and the airport as tuples to a new list.
By calling the sort function on this list of tuples the list should be sorted by the first value of the pair.
After this there are multiple ways to reduce the list to only 10 values.

**Submit as:** exercise_d.py