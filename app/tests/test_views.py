import pytest

def validate_user(username, password):
    if username == "admin" and password == "1234":
        return {"status": "success", "message": "User validated"}
    else:
        return {"status": "error", "message": "Invalid credentials"}

def finalize_order(order_id):
    if order_id == 101:
        return {"status": "success", "message": "Order finalized"}
    else:
        return {"status": "error", "message": "Order not found"}

def test_validate_user():
    result = validate_user("admin", "1234")
    assert result == {"status": "success", "message": "User validated"}

    result = validate_user("user", "wrongpassword")
    assert result == {"status": "error", "message": "Invalid credentials"}

def test_finalize_order():
    result = finalize_order(101)
    assert result == {"status": "success", "message": "Order finalized"}

    result = finalize_order(999)
    assert result == {"status": "error", "message": "Order not found"}
