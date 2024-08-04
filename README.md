# Django Todo App

A simple, lightweight Todo application built with Django and SQLite.

## Features

- Create, read, update, and delete todo items
- Mark tasks as complete/incomplete
- User authentication
- Responsive design

## Tech Stack

- Django
- SQLite
- HTML/CSS
- Bootstrap (optional)

## Prerequisites

- Python 3.x
- pip

## Installation

1. Clone the repository:  git clone https://github.com/alimkb/django-todo.git

2. Create a virtual environment:  
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations:
python manage.py migrate

5. Create a superuser (optional):
python manage.py createsuperuser

## Usage

1. Start the development server:
python manage.py runserver

2. Open a web browser and navigate to `http://localhost:8000`

3. Log in or register to start managing your todos

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

