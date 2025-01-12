# Food Delivery App

This repository contains the source code for a **Food Delivery App** built using the Django framework. The app serves as a backend system for managing users, restaurants, orders, and deliveries in a food delivery ecosystem.

---

## Features

1. **User Management**:
   - Supports different roles: Customer, Restaurant Owner, Delivery Agent.
   - Role-based authentication and authorization.
   
2. **Restaurant Management**:
   - Add, update, and manage restaurant details.
   - Menu management.

3. **Order Management**:
   - Create, update, and track orders.
   - Manage order statuses.

4. **Delivery Management**:
   - Assign delivery agents to orders.
   - Track delivery status.

5. **Real-time Notifications**:
   - WebSocket-based notifications for order updates (future implementation).

6. **API-Driven Architecture**:
   - RESTful APIs for seamless front-end integration.

---

## Folder Structure

```plaintext
food_delivery_app/
├── food_delivery_app/       # Main project folder
│   ├── settings/            # Django settings for different environments
│   │   ├── base.py          # Common settings
│   │   ├── dev.py           # Development settings
│   │   ├── prod.py          # Production settings
│   ├── urls.py              # URL routing for the project
│   ├── wsgi.py              # WSGI entry point for deployment
│   ├── asgi.py              # ASGI entry point for WebSocket support
├── apps/                    # Application modules
│   ├── accounts/            # User and authentication management
│   ├── restaurants/         # Restaurant-specific features
│   ├── orders/              # Order creation and management
│   ├── deliveries/          # Delivery agent and tracking
│   ├── core/                # Reusable utilities and base models
├── templates/               # HTML templates for rendering (if required)
├── static/                  # Static files (CSS, JS, images)
├── media/                   # Uploaded media files (e.g., profile pictures)
├── manage.py                # Django CLI entry point
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── .env                     # Environment variables
├── README.md                # Documentation
```

---

## Installation

### Prerequisites
- Python 3.8+
- pip
- Docker (optional, for containerized setup)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/food_delivery_app.git
   cd food_delivery_app
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Update the database configuration in `settings/dev.py` and run:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000`.

---

## Usage

- **Admin Panel**: Accessible at `/admin` for managing users, restaurants, and orders.
- **API Endpoints**:
  - `/accounts/users/` - Manage user data.
  - `/restaurants/` - Manage restaurant data (future implementation).
  - `/orders/` - Manage orders (future implementation).

---

## Docker Setup

1. **Build and Start Containers**:
   ```bash
   docker-compose up --build
   ```

2. **Access the App**:
   The app will be available at `http://localhost:8000`.

---

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

---

## Future Enhancements

- Implement real-time WebSocket support for live order updates.
- Add payment gateway integration.
- Enhance delivery tracking with geolocation.
- Introduce advanced filters and reporting for admins.

