# Directus Python API

Simple Python3 wrapper for the Directus API

## Install

Simply install the package from the root directory with:

```
pip install .
```

## Usage
```python
from directus_api import DirectusClient

url = "http://123.45.678.90:8080"
project = "Directus"

# Creates a Directus client object
client = DirectusClient(url, project)

# Create a Directus client from a user (generates access token)
client = DirectusClient(url, project, email="email@example.com", password="password")

# Get a list of all items in a collection
client.get_items_list("photos")

# Get a specific item in a collection by id
client.get_item("photos", 1)

# Get a list of all files (requires full constructor with email and password)
client.get_files_list()

# Get a specific file (requires full constructor with email and password)
client.get_file(1)

# Create a new item in a collection (requires full constructor with email and password)
item = {name: "Directus", id: 1}
client.create_item("collection_name", item)
```