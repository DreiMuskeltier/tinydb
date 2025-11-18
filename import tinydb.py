from tinydb import TinyDB
from tinydb import Query

db = TinyDB('C:/Users/mfied/Pythonprojekte/Challenge 2 NoSQL/db.json')

# Insert a single document
db.insert({'name': 'John', 'age': 22})

# Insert multiple documents
db.insert_multiple([
{'name': 'Jane', 'age': 25},
{'name': 'Doe', 'age': 30}
])

User = Query()

# Search for documents where the name is 'John'
results = db.search(User.name == 'John')
print(results)

db.update({'age': 23}, User.name == 'John')

db.remove(User.name == 'John')

from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

# Use a caching middleware with JSON storage
db = TinyDB('db.json', storage=CachingMiddleware(JSONStorage))

# Create a new table
table = db.table('new_table')
table.insert({'value': True})