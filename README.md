# QStack Backend

This is the backend for the QStack application, a powerful and scalable web application built with Python, Django, and the Django Rest Framework. This backend provides a robust API for handling contact form submissions, providing website improvement suggestions, and managing user authentication with JSON Web Tokens.

## Features

- **Contact Form API**: A secure endpoint to collect and store contact form submissions from users.
- **Suggestions API**: A simple API that provides a list of suggestions for improving a website's performance and user experience.
- **JWT Authentication**: A complete and secure authentication system using JSON Web Tokens, including endpoints for obtaining and refreshing tokens.
- **Scalable Architecture**: A clean and organized project structure that is easy to extend and maintain.
- **CORS Configuration**: Pre-configured Cross-Origin Resource Sharing (CORS) settings to allow requests from your frontend application.

## Security Note

**Warning:** This project contains a `password.txt` file which is a major security risk. Storing passwords in plaintext is insecure. It is strongly recommended to remove this file and implement a secure authentication method.

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd qstack-backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root of the project and add the following variables:
   ```
   DATABASE_URL=<your-database-url>
   SECRET_KEY=<your-secret-key>
   DEBUG=<True-or-False>
   ALLOWED_HOSTS=<your-allowed-hosts>
   ```

5. **Apply the database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- **Admin Panel**: `/admin/`
- **Contact Form**: `POST /api/contact/`
- **Suggestions**: `GET /api/suggestions/`
- **Obtain JWT Token**: `POST /api/token/`
- **Refresh JWT Token**: `POST /api/token/refresh/`

## Project Structure

```
.
├── manage.py
├── requirements.txt
├── src
│   ├── settings.py
│   └── urls.py
├── main
│   ├── models.py
│   ├── serializers.py
│   └── contact
│       ├── urls.py
│       └── views.py
└── api
    ├── urls.py
    └── views.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

