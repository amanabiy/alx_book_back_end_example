# Django CRUD Book Back-End System

This is a simple CRUD (Create, Read, Update, Delete) application for managing books using Django and Django REST Framework.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd book_crud
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for accessing the admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Add a new package or library:**
   ```bash
   pip install <package-name>
   ```

8. **Update requirements.txt:**
   After adding a new package, run:
   ```bash
   pip freeze > requirements.txt
   ```

## Running the Application

To start the development server, run:
    ```bash
    python manage.py runserver
    ```

You can access the application at:
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (Admin panel)
- [http://127.0.0.1:8000/api/books/](http://127.0.0.1:8000/api/books/) (API endpoint for books)
- [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) (Swagger UI)
- [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) (ReDoc Documentation)


## Links to Documentation

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

