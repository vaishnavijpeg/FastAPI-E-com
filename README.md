# E-Commerce Platform APIs-  Functional Requirements :

## Authentication
- Users can register as customer or seller
- Registered users can login and receive an authentication token
- Passwords are securely hashed before storage
- Authenticated users can access protected routes using JWT tokens
- Role-based permissions are supported (seller vs customer)

## Users
- Users can register
- Users can login
- Users can view their profile
- Users can view other users
- Sellers can list products they own
- Customers can manage their cart
- Users can place orders

## Products
- Users can fetch all products
- Users can fetch a single product
- Sellers can create products
- Sellers can update their products
- Sellers can delete their products
- Products belong to a seller
- Products contain pricing information

## Cart
- Users can create a cart automatically
- Users can add products to their cart
- Users can update product quantity in cart
- Users can remove products from cart
- Users can view their cart
- A cart can contain multiple products

## Orders
- Users can checkout their cart
- Checkout creates an order
- Orders store purchased products
- Orders store total price
- Users can view their order history
- Orders contain order items with product and quantity

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- JSON Web Token

# Entities
  
## User
- id
- name
- email
- password (hashed)
- role (customer / seller)
- created_at
- updated_at

## Product
- id
- name
- description
- price
- seller_id // reference to user
- created_at
- updated_at

## Cart
- id
- user_id // reference to user
- created_at
- updated_at

## CartItem
- id
- cart_id // reference to cart
- product_id // reference to product
- quantity
- created_at
- updated_at

## Order
- id
- user_id // reference to user
- total_price
- created_at
- updated_at

## OrderItem
- id
- order_id // reference to order
- product_id // reference to product
- quantity
- price_at_purchase
- created_at
- updated_at

# Mapping Entities
- ## Cart - Product (CartItems)
- cart_id
- product_id
- quantity

- This mapping represents the many-to-many relationship between carts and products.

# Order - Product (OrderItems)
- order_id
- product_id
- quantity
- price_at_purchase

- This mapping stores the products purchased in each order.



