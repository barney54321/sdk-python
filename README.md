<p align="center">
  <a href="https://directus.io" target="_blank" rel="noopener noreferrer">
    <img src="https://user-images.githubusercontent.com/522079/43096167-3a1b1118-8e86-11e8-9fb2-7b4e3b1368bc.png" width="140" alt="Directus Logo"/>
  </a>
</p>

<h1 align="center">
  Directus Python SDK
</h1>

<h3 align="center">
  <a href="https://directus.io">Website</a> • 
  <a href="https://docs.directus.io">Docs</a> • 
  <a href="https://docs.directus.io/api/reference.html">API Reference</a> • 
  <a href="https://docs.directus.io/app/user-guide.html">User Guide</a> • 
  <a href="https://directus.app">Demo</a> • 
  <a href="https://docs.directus.io/supporting-directus.html">Contribute</a>
</h3>

<p>&nbsp;</p>

> _This codebase is a work-in-progress. The repo is here as a placeholder for anyone interested in contributing to the software development kit. Pull-requests and contributions are welcome!_

<p>&nbsp;</p>

## Installation

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

<p>&nbsp;</p>

----

<p align="center">
  Directus is released under the <a href="http://www.gnu.org/copyleft/gpl.html">GPLv3</a> license. <a href="http://rangerstudio.com">RANGER Studio LLC</a> owns all Directus trademarks and logos on behalf of our project's community. Copyright © 2006-2018, <a href="http://rangerstudio.com">RANGER Studio LLC</a>.
</p>