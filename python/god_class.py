"""Code smell: God Class — one class that knows and does everything."""


class ApplicationManager:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []
        self.db_connection = None
        self.email_server = None
        self.log_file = "app.log"
        self.config = {}

    # --- Database ---
    def connect_db(self, host, port, name):
        self.db_connection = f"{host}:{port}/{name}"

    def disconnect_db(self):
        self.db_connection = None

    def run_query(self, sql):
        print(f"Running: {sql} on {self.db_connection}")

    # --- User management ---
    def create_user(self, name, email, password):
        user = {"id": len(self.users) + 1, "name": name, "email": email, "password": password}
        self.users.append(user)
        return user

    def delete_user(self, user_id):
        self.users = [u for u in self.users if u["id"] != user_id]

    def get_user(self, user_id):
        return next((u for u in self.users if u["id"] == user_id), None)

    def authenticate_user(self, email, password):
        return next((u for u in self.users if u["email"] == email and u["password"] == password), None)

    # --- Product management ---
    def add_product(self, name, price, stock):
        product = {"id": len(self.products) + 1, "name": name, "price": price, "stock": stock}
        self.products.append(product)
        return product

    def update_stock(self, product_id, quantity):
        for p in self.products:
            if p["id"] == product_id:
                p["stock"] += quantity

    def get_products_on_sale(self):
        return [p for p in self.products if p.get("on_sale")]

    # --- Order management ---
    def place_order(self, user_id, product_id, quantity):
        order = {"id": len(self.orders) + 1, "user_id": user_id, "product_id": product_id, "quantity": quantity}
        self.orders.append(order)
        return order

    def cancel_order(self, order_id):
        self.orders = [o for o in self.orders if o["id"] != order_id]

    def get_user_orders(self, user_id):
        return [o for o in self.orders if o["user_id"] == user_id]

    # --- Email ---
    def send_email(self, to, subject, body):
        print(f"Email to {to}: {subject}\n{body}")

    def send_order_confirmation(self, order_id):
        order = next((o for o in self.orders if o["id"] == order_id), None)
        if order:
            user = self.get_user(order["user_id"])
            self.send_email(user["email"], "Order Confirmed", f"Order #{order_id} confirmed.")

    # --- Logging ---
    def log(self, message):
        with open(self.log_file, "a") as f:
            f.write(message + "\n")

    def log_error(self, error):
        self.log(f"ERROR: {error}")

    def log_info(self, info):
        self.log(f"INFO: {info}")

    # --- Config ---
    def load_config(self, path):
        import json
        with open(path) as f:
            self.config = json.load(f)

    def get_config(self, key):
        return self.config.get(key)

    # --- Reporting ---
    def generate_sales_report(self):
        total = sum(
            next((p["price"] for p in self.products if p["id"] == o["product_id"]), 0) * o["quantity"]
            for o in self.orders
        )
        print(f"Total sales: ${total:.2f}")

    def generate_user_report(self):
        print(f"Total users: {len(self.users)}")
