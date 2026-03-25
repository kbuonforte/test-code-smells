"""Code smell: Inappropriate Intimacy — classes that pry too deeply into each other."""


class Cart:
    def __init__(self):
        self._items = []         # "private"
        self._coupon = None      # "private"
        self._user_id = None     # "private"

    def add_item(self, item):
        self._items.append(item)

    def set_coupon(self, coupon):
        self._coupon = coupon

    def set_user(self, user_id):
        self._user_id = user_id


class OrderProcessor:
    """Directly manipulates Cart internals instead of going through its interface."""

    def process(self, cart, payment):
        # Reaching into Cart's private state
        if not cart._items:
            raise ValueError("Cart is empty")

        subtotal = sum(i["price"] * i["qty"] for i in cart._items)

        # Directly reading and interpreting private coupon logic
        discount = 0
        if cart._coupon == "HALF":
            discount = subtotal * 0.50
        elif cart._coupon and cart._coupon.startswith("PCT"):
            pct = int(cart._coupon[3:])
            discount = subtotal * (pct / 100)

        total = subtotal - discount

        # Directly mutating Cart's private list after checkout
        cart._items = []
        cart._coupon = None

        return {"user": cart._user_id, "total": total, "payment": payment}

    def get_item_count(self, cart):
        # Should call a public method, not touch internals
        return len(cart._items)

    def apply_bulk_discount(self, cart):
        # Directly mutating items in another class's private list
        for item in cart._items:
            if item["qty"] >= 5:
                item["price"] *= 0.90


class Config:
    def __init__(self):
        self._settings = {}
        self._overrides = {}
        self._env = "production"

    def set(self, key, value):
        self._settings[key] = value


class FeatureFlags:
    """Depends on Config internals rather than its public interface."""

    def __init__(self, config):
        self.config = config

    def is_enabled(self, flag):
        # Bypasses Config's public API to reach into private dicts
        override = self.config._overrides.get(flag)
        if override is not None:
            return override
        if self.config._env == "production":
            return self.config._settings.get(flag, False)
        return True  # all flags on in non-prod

    def list_all(self):
        # Merging two private dicts from another class
        merged = {**self.config._settings, **self.config._overrides}
        return {k: v for k, v in merged.items() if isinstance(v, bool)}
