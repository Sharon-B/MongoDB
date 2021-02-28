import os
import pymongo
if os.path.exists("env.py"):
    import env                      # If env.py file exists import environment to grab the hiddden environment variables


# Set 3 constant variables at top to make code cleaner
# Python constants are written in all caps with _ to separate any words
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "firstDB"
COLLECTION = "celebs"


# Function to connect our database:
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn                                     # return our connection object
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e   # using placeholder %s to contain the error message e


conn = mongo_connect(MONGO_URI)     # Call our mongo_connect function passing our hidden MONGO_URI variable as the url argument

coll = conn[DATABASE][COLLECTION]   # Set our collection name which will be the connection object with our db and collection variables

""" Insert a single document
new_doc = {
    "first": "douglas",
    "last": "adams",
    "dob": "11/03/1952",
    "gender": "m",
    "hair_color": "grey",
    "occupation": "writer",
    "nationality": "british"}

coll.insert(new_doc)        # insert new_doc record/document into the DB

# Insert multiple documents
new_docs = [{
    "first": "terry",
    "last": "pratchett",
    "dob": "28/04/1948",
    "gender": "m",
    "hair_color": "not much",
    "occupation": "writer",
    "nationality": "british"
}, {
    "first": "george",
    "last": "rr martin",
    "dob": "20/09/1948",
    "gender": "m",
    "hair_color": "white",
    "occupation": "writer",
    "nationality": "american"
}]

coll.insert_many(new_docs) """

coll.update_many({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

documents = coll.find()     # variable documents set to find all items from the celebs collection, returns a MongoDB object ie a Cursor
                            # so we need to iterate over that data to unpack it:

for doc in documents:       # iteration of the documents variable to unpack the data
    print(doc)
