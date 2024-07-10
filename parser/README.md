# Getting started with a Python application

## Available Scripts

In the project directory, you can run:

### `docker compose up`

Runs a dockerfile which executes the commands: `parser.py 1` and `get_data.py`

### `parser.py [int]`

Executed with a number argument.\
The number is the number of pages that need to be processed on the [https://www.house.kg/](https://www.house.kg/kupit-kvartiru?rooms=3&region=1&town=2&price_from=30%27f%2700000&currency=1&sort_by=upped_at%20desc&page=1) website

### `get_data.py`

Provides data on apartments in Bishkek in sorted form

### `create_table_apartmants.py`

Creates a table apartments

### `delete_table.py`

Deletes the apartments table
