# Django E-commerce Website

## Overview
This is a basic e-commerce website built using Django. It includes essential features such as product listing, product details, a shopping cart, and a checkout process.

## Features
- **Home Page (Index Page)**: Displays products with pagination.
- **Product Detail Page**: Shows individual product details.
- **Shopping Cart**: Users can add products to a cart using localStorage.
- **Checkout Page**: Users enter shipping details and confirm their orders.

## Project Structure
```
shop/
    ├── templates/
    │   ├── shop/
    │   │   ├── index.html
    │   │   ├── detail.html
    │   │   ├── checkout.html
    ├── views.py
    ├── urls.py
    ├── models.py
```

## URL Routing
```python
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
]
```

## Templates
### `index.html`
- Displays product listings with images, names, and prices.
- Pagination for browsing multiple products.
- JavaScript for handling cart functionality using localStorage.

### `detail.html`
- Shows product details including image, title, price, discount, and description.

### `checkout.html`
- Displays the cart summary.
- Collects user shipping details and submits them for processing.

## JavaScript (Cart Management)
- Uses `localStorage` to store cart items.
- Updates total price dynamically.
- Handles add-to-cart functionality.

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd django-ecommerce
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Django server:
   ```bash
   python manage.py runserver
   ```
4. Access the application at `http://127.0.0.1:8000/`.

## Future Enhancements
- User authentication (login/logout functionality).
- Order history and payment integration.
- Improved cart UI and database-backed cart system.

## License
This project is open-source and available under the MIT License.

