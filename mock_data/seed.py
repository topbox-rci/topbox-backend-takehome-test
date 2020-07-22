from app.helpers import mongo_client

db = mongo_client()
names = db.list_collection_names()

# Create Mongo Collections
if 'clients' not in names:
    db.create_collection('clients')

if 'engagements' not in names:
    db.create_collection('engagements')

if 'interactions' not in names:
    db.create_collection('interactions')

# Seed Users
db.clients.delete_many({})
client1 = db.clients.insert_one({'name': 'Unicorns, LLC', 'nickname': 'uni'}).inserted_id
client2 = db.clients.insert_one({'name': 'Giraffes, Ltd.', 'nickname': 'raf'}).inserted_id

# Seed Engagements
db.engagements.delete_many({})
client1_engagement1 = db.engagements.insert_one({'clientId': client1, 'name': 'Phone'}).inserted_id
client1_engagement2 = db.engagements.insert_one({'clientId': client1, 'name': 'Chat Support'}).inserted_id

client2_engagement1 = db.engagements.insert_one({'clientId': client2, 'name': 'Phone Support'}).inserted_id
client2_engagement2 = db.engagements.insert_one({'clientId': client2, 'name': 'Twitter'}).inserted_id
client2_engagement3 = db.engagements.insert_one({'clientId': client2, 'name': 'Facebook'}).inserted_id

# Seed Interaction data
