import models
from fastapi import HTTPException


def create_user(db, user):
    try:
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

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")


def create_product(db, product):
    try:
        db_product = models.Product(
            name=product.name,
            price=product.price
        )

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating product: {str(e)}")


def add_to_cart(db, user_id, item):
    try:
        cart_item = models.CartItem(
            user_id=user_id,
            product_id=item.product_id,
            quantity=item.quantity
        )

        db.add(cart_item)
        db.commit()
        db.refresh(cart_item)

        return cart_item

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error adding item to cart: {str(e)}")


def checkout_cart(db, user_id):
    try:
        items = db.query(models.CartItem).filter(
            models.CartItem.user_id == user_id
        ).all()

        if not items:
            raise HTTPException(status_code=404, detail="Cart is empty")

        total = 0

        for item in items:
            product = db.query(models.Product).filter(
                models.Product.id == item.product_id
            ).first()

            if not product:
                raise HTTPException(
                    status_code=404,
                    detail=f"Product with id {item.product_id} not found"
                )

            total += product.price * item.quantity

        return {
            "user_id": user_id,
            "total_price": total,
            "items": len(items)
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Checkout failed: {str(e)}")
