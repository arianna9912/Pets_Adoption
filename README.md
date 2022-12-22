# Adoption Pets project

This is a project of adoption pets.


## Compatibility

Linux, macOS, and Windows!


## Requirements

- Python 3.9
- Django 4


## Installation

1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
2. Create migration and migrate database
    ```bash
    py manage.py makemigrations mypets
    py manage.py migrate
    ```
3. Create admin user
    ```bash
    py manage.py createsuperuser
    ```
4. Run server
    ```bash
    py manage.py runserver 8000
    ```
5. Access with browser to: `http://127.0.0.1:8000/`


## License

This project is licensed under the terms of the MIT license.
