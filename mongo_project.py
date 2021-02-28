import os
import pymongo
if os.path.exists("env.py"):
    import env


# Set 3 constant variables at top to make code cleaner
# Python constants are written in all caps with _ to separate any words
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "firstDB"
COLLECTION = "celebs"


# Function to connect our database:
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit the menu")

    option = input("Enter an option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:         # If no docs are returned an empty cursor object will be returned ie if not doc
        print("")
        print("Error! No results found.")

    return doc          # return our doc cursor object either empty or with a result


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {
        "first": first.lower(),     # storing first & last as lower case to make it easier for finding items later
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")   # ideally should catch the specific error but this will do for now.


def main_loop():
    while True:
        option = show_menu()        # Call show_menu function and assign it to a variable called option
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)     # Call our mongo_connection function
coll = conn[DATABASE][COLLECTION]   # Call our collection
main_loop()                         # Call our main_loop function
