# Django Search Application

This repository contains a Django search application that allows users to search for dish names and view matching results.

## Requirements

### 1. Working Code with `requirements.txt`

The project is built using Django, and the `requirements.txt` file lists all necessary dependencies.

#### `requirements.txt`

```plaintext
Django~=3.0
```

To install dependencies, run:

```bash
pip install -r requirements.txt
```

### 2. Working SQLite Database File

The SQLite database (`db.sqlite3`) contains restaurant data loaded from the `restaurants_small.csv` file using a custom management command.

### 3. Image of the Working App with a Search Query and Its Results

<img src="assets/images/dark mode preview.png">

## Usage

- Enter a dish name in the search box and press Enter or click "Search".
- View the search results displayed on the page.

## Directory Structure

```plaintext
dish_search_project/
├── searchapp/
│   ├── migrations/
│   ├── templates/
│   ├── management/
│   │   └── commands/
│   │       └── load_restaurants.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Additional Notes

- Ensure `restaurants_small.csv` is placed in the appropriate directory (`searchapp/static/csv/`) before running the data loading command ('python manage.py load_restaurants').
- Customize the application further as per specific requirements or additional features.
