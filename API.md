# API Endpoints

## Authentication

| Method | Endpoint      | Description                                  | Auth Required |
|--------|--------------|-----------------------------------------------|---------------|
| POST   | `/register`  | Register a new user (customer or seller)        | No |
| POST   | `/login`     | Login user and receive JWT access token         | No |

---

##  Users

| Method | Endpoint              | Description                    | Auth Required |
|--------|-----------------------|--------------------------------|---------------|
| GET    | `/users`              | Fetch all users                | No |
| GET    | `/users/{user_id}`    | Fetch single user profile      | No |
| PUT    | `/users/{user_id}`    | Update user profile            | Yes|

---

##  Products

| Method | Endpoint                      | Description                                 | Auth Required |
|--------|-------------------------------|---------------------------------------------|---------------|
| GET    | `/products`                   | Fetch all products                          |  No |
| GET    | `/products/{product_id}`      | Fetch single product                        |  No |
| POST   | `/products`                   | Create new product (Seller only)            |  Yes |
| PUT    | `/products/{product_id}`      | Update existing product                     |  Yes |
| DELETE | `/products/{product_id}`      | Delete product                              |  Yes |

---

##  Cart

| Method | Endpoint                                      | Description                          | Auth Required |
|--------|-----------------------------------------------|--------------------------------------|---------------|
| GET    | `/cart/{user_id}`                             | Get user's cart                     |  Yes |
| POST   | `/cart/{user_id}/add`                         | Add product to cart                 |  Yes |
| PUT    | `/cart/{user_id}/update`                      | Update product quantity in cart     |  Yes |
| DELETE | `/cart/{user_id}/remove/{product_id}`         | Remove product from cart            |  Yes |

---

##  Orders

| Method | Endpoint                    | Description                              | Auth Required |
|--------|----------------------------|------------------------------------------|---------------|
| POST   | `/checkout/{user_id}`      | Checkout cart and create order           |  Yes |
| GET    | `/orders/{user_id}`        | Get user's order history                 |  Yes |
| GET    | `/orders/details/{order_id}` | Get specific order details             |  Yes |

---

#  Authentication Header

Protected endpoints require a JWT token in the request header, Authorization: Bearer <access_token>
The access token is generated during login.

## POST /products
- Authorization: Bearer <access_token>
- Content-Type: application/json

{
"name": "Laptop",
"price": 1200,
"seller_id": 2
}

#  API Documentation

- After running the server, visit:
http://127.0.0.1:8000/docs
