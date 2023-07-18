from pymongo import MongoClient
from pandas import DataFrame
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://noufalrahim24:Noufal_Rahim1@cluster0.wuujoyu.mongodb.net/ReviewDB"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['ReviewDB']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   collection_name = dbname["reviews"]
   item_details = collection_name.find()
   items_df = DataFrame(item_details)
   print(items_df)
   items_df.to_csv("Data.csv")