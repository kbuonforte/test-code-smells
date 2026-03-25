"""Code smell: Long Method — does too many things in one function."""


def process_order(order):
    # Validate order
    if not order:
        return None
    if "items" not in order:
        return None
    if len(order["items"]) == 0:
        return None
    for item in order["items"]:
        if "price" not in item:
            return None
        if item["price"] < 0:
            return None
        if "quantity" not in item:
            return None
        if item["quantity"] <= 0:
            return None

    # Calculate subtotal
    subtotal = 0
    for item in order["items"]:
        subtotal += item["price"] * item["quantity"]

    # Apply discount
    discount = 0
    if subtotal > 100:
        discount = subtotal * 0.10
    elif subtotal > 50:
        discount = subtotal * 0.05
    subtotal -= discount

    # Calculate tax
    tax_rate = 0.08
    if order.get("state") == "CA":
        tax_rate = 0.0925
    elif order.get("state") == "TX":
        tax_rate = 0.0825
    elif order.get("state") == "NY":
        tax_rate = 0.08875
    tax = subtotal * tax_rate

    # Calculate shipping
    shipping = 0
    if subtotal < 25:
        shipping = 7.99
    elif subtotal < 50:
        shipping = 4.99
    else:
        shipping = 0

    # Build receipt
    total = subtotal + tax + shipping
    receipt = {
        "items": order["items"],
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "shipping": shipping,
        "total": round(total, 2),
    }

    # Send confirmation email
    customer_email = order.get("email", "")
    if customer_email:
        subject = "Order Confirmation"
        body = f"Thank you for your order! Total: ${total:.2f}"
        print(f"Sending email to {customer_email}: {subject} — {body}")

    return receipt
