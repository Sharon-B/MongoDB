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


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
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
main_loop()
