# Ecommerce Backend

A REST API backend for an ecommerce platform built with Django and Django REST Framework.

## Tech Stack

- Python 3.10+
- Django 5.2
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (development)
- Pillow (image uploads)
- django-cors-headers

## Setup

```bash
# Clone the repo
git clone https://github.com/your-username/ecommerce-backend-design.git
cd ecommerce-backend-design

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed sample data
python manage.py seed_data

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## API Endpoints

### Products

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/products/` | No | List all products (paginated) |
| GET | `/api/products/?search=<query>` | No | Search by name or category |
| GET | `/api/products/?page=2` | No | Paginate (10 per page) |
| POST | `/api/products/` | JWT | Add a new product |
| GET | `/api/products/<id>/` | No | Get product detail |
| PUT | `/api/products/<id>/` | JWT | Update a product |
| DELETE | `/api/products/<id>/` | JWT | Delete a product |
| GET | `/api/categories/` | No | List all categories |
| POST | `/api/categories/` | JWT | Create a category |

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and receive JWT tokens |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| GET | `/api/auth/profile/` | Get current user profile |
| PUT | `/api/auth/profile/` | Update current user profile |

### Cart (JWT required)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/cart/` | View current cart |
| POST | `/api/cart/add/` | Add item to cart |
| DELETE | `/api/cart/remove/<id>/` | Remove item from cart |

### Orders (JWT required)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/orders/` | List your orders |
| POST | `/api/orders/place/` | Checkout (converts cart to order) |

### Admin

Django admin panel available at `/admin/`.

## Request Examples

**Register**
```json
POST /api/auth/register/
{
  "username": "john",
  "email": "john@example.com",
  "password": "secret123"
}
```

**Login**
```json
POST /api/auth/login/
{
  "username": "john",
  "password": "secret123"
}
```
Response includes `access` and `refresh` JWT tokens.

**Add Product** (requires `Authorization: Bearer <access_token>`)
```json
POST /api/products/
{
  "name": "Laptop",
  "price": "999.99",
  "category": 1,
  "description": "High performance laptop",
  "stock": 10
}
```

**Add to Cart** (requires `Authorization: Bearer <access_token>`)
```json
POST /api/cart/add/
{
  "product_id": 1,
  "quantity": 2
}
```

**Place Order** — converts current cart into an order (no body needed)
```
POST /api/orders/place/
```

## Project Structure

```
ecommerce-backend/
├── manage.py
├── requirements.txt
├── ecommerce/ecommerce/      # Django project settings & URLs
├── store/                    # Products & categories app
│   └── management/commands/seed_data.py
└── userauth/                 # Registration, login, profile
```
