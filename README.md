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

<img src="Django Search Application/dish_search_app/searchapp/static/Screenshot 2024-06-19 183002.png">
<img src="Django Search Application/dish_search_app/searchapp/static/Screenshot 2024-06-19 183029.png">

---

Replace `search_app_screenshot.png` with the actual filename of your screenshot showing the app's search functionality in action.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone [<repository-url>](https://github.com/priyamjha/Django-Search-Application.git)
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations and load data:

   ```bash
   python manage.py migrate
   python manage.py load_restaurants
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Open a web browser and navigate to `http://127.0.0.1:8000/` to view the application.

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

- Ensure `restaurants_small.csv` is placed in the appropriate directory (`searchapp/static/csv/`) before running the data loading command.
