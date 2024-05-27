# Dear Diary

Dear Diary is a simple notes web application built using Flask. Users can sign up, log in, and manage personal notes.

## Features

- User authentication (sign up, log in, log out)
- Create, view, and delete notes
- Responsive design using Bootstrap

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/ybaweja04/Dear-Diary.git
    cd Dear-Diary
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**

    Create a `.env` file in the project root and add the following:

    ```ini
    SECRET_KEY=your_secret_key_here
    DATABASE_URI=sqlite:///database.db
    ```

5. **Set up the database**

    ```bash
    flask shell
    >>> from yourapp import db
    >>> db.create_all()
    >>> exit()
    ```

### Running the Application

1. **Set the FLASK_APP environment variable**

    ```bash
    export FLASK_APP=main   # On Windows: `set FLASK_APP=main`
    ```

2. **Run the Flask development server**

    ```bash
    flask run
    ```

3. **Visit**

    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

- `main.py`: Entry point for the application
- `auth.py`: Handles authentication routes
- `models.py`: Contains database models
- `views.py`: Contains main application routes
- `__init__.py`: Initializes the Flask application
- `templates/`: Contains HTML templates
- `static/`: Contains static files like CSS and JavaScript
