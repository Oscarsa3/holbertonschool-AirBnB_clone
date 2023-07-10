![](https://res.cloudinary.com/djvwjnzxw/image/upload/v1688789698/airbnb-holberton_mx2ss7.png)
# Airbnb Clone - The Console

## Table of Content
* [Description](#description)
* [Technical concepts](#technical-concepts)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#how-to-use-the-console)
* [Authors](#authors)
* [License](#license)

## Description
For this first part of the project called AirBnB clone, what we are implementing are some base classes and in addition to this we developed a command interpreter that we will call console. This console will be able to receive and execute arguments such as create, destroy, update, all, show, quit and must react as desired to the EOF.

## Technical concepts
Some technical concepts that we were acquiring while this project was carried out until this part are: for example we were able to clarify the doubts of how to work when importing the cmd module. We saw how it works with its methods that are already pre-established, we have also worked importing the unittest module and that is where we had some problems with some tests for methods that we could not pass but with a cold head we could decipher them and move forward with it. We have worked importing the os module, which allows us to verify if there are specific files that we should evaluate. Many concepts that if you see the complete code you can analyze and see what I am talking about.

## Installation
* Clone this repository: `git clone "https://github.com/Oscarsa3/holbertonschool-AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* `def reload(self)` -  deserializes the JSON file to __objects

[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `create` - Create an instance with any of the implemented classes and prints the id
* `destroy` - Deletes an instance based on the class name and id. 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file
* Update attributes of an object
* Destroy an object

## How to use the console
To be able to use our console we must follow these steps:
1) Be inside our repository `cd holbertonschool-AirBnB_clone/`
2) Verify that our console.py file exists and is executable
3) Then we need to run our file. `./console.py`
4) A promp like this should appear

![](https://i.ibb.co/GRQmZhK/promp.jpg)

5) We wrote some arguments and it should look like this.

![](https://i.ibb.co/XSRmKcy/args.jpg)

## Authors
* Oscar Salinas - [Github](https://github.com/Oscarsa3)

## License
Public Domain. No copy write protection. 
