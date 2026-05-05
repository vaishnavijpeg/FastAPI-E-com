import models


def create_user(db, user):
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_product(db, product):
    db_product = models.Product(
        name=product.name,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def add_to_cart(db, user_id, item):
    cart_item = models.CartItem(
        user_id=user_id,
        product_id=item.product_id,
        quantity=item.quantity
    )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item


def checkout_cart(db, user_id):
    items = db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()
    total = 0

    for item in items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        total += product.price * item.quantity

    return {"total_price": total}
