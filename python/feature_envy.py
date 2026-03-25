"""Code smell: Feature Envy — a method that's more interested in another class's data."""


class Customer:
    def __init__(self, name, email, loyalty_points, membership_tier, purchase_history):
        self.name = name
        self.email = email
        self.loyalty_points = loyalty_points
        self.membership_tier = membership_tier
        self.purchase_history = purchase_history


class Order:
    def __init__(self, items, customer):
        self.items = items
        self.customer = customer
        self.discount = 0
        self.total = 0

    def calculate_discount(self):
        """This method is obsessed with Customer's data — it belongs on Customer."""
        discount = 0

        if self.customer.membership_tier == "gold":
            discount += 0.15
        elif self.customer.membership_tier == "silver":
            discount += 0.10
        elif self.customer.membership_tier == "bronze":
            discount += 0.05

        if self.customer.loyalty_points > 1000:
            discount += 0.05
        elif self.customer.loyalty_points > 500:
            discount += 0.02

        if len(self.customer.purchase_history) > 10:
            discount += 0.03

        if self.customer.membership_tier == "gold" and self.customer.loyalty_points > 500:
            discount += 0.02  # bonus stacking

        self.discount = min(discount, 0.30)
        return self.discount

    def format_confirmation_email(self):
        """Also envious — mostly just reads Customer fields."""
        greeting = f"Dear {self.customer.name},"
        account_info = f"Account: {self.customer.email} | Tier: {self.customer.membership_tier}"
        points_msg = f"You have {self.customer.loyalty_points} loyalty points."
        history_msg = f"This is order #{len(self.customer.purchase_history) + 1} with us."
        return f"{greeting}\n{account_info}\n{points_msg}\n{history_msg}"


class Warehouse:
    def __init__(self, inventory):
        self.inventory = inventory  # dict: product_id -> {stock, location, weight, fragile}

    def prepare_shipment(self, order):
        """More feature envy — reads deeply into Order and its items."""
        lines = []
        for item in order.items:
            product = self.inventory.get(item["product_id"])
            if product:
                location = product["location"]
                weight = product["weight"] * item["quantity"]
                fragile = product["fragile"]
                lines.append(
                    f"Pick {item['quantity']}x {item['product_id']} "
                    f"from {location} (weight: {weight}kg, fragile: {fragile})"
                )
        return lines
