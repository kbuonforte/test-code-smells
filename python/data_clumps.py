"""Code smell: Data Clumps — groups of data that always travel together."""


# These three always appear together — should be a Money or Price class
def add_prices(amount1, currency1, amount2, currency2):
    if currency1 != currency2:
        raise ValueError("Currency mismatch")
    return amount1 + amount2, currency1


def format_price(amount, currency, locale):
    symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def convert_price(amount, currency, locale, target_currency, rates):
    rate = rates.get((currency, target_currency), 1.0)
    return amount * rate, target_currency, locale


# lat/lng always together — should be a Coordinate or GeoPoint class
def distance_between(lat1, lng1, lat2, lng2):
    import math
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def is_within_radius(lat1, lng1, lat2, lng2, radius_km):
    return distance_between(lat1, lng1, lat2, lng2) <= radius_km


def find_nearest(lat, lng, locations):
    """locations: list of (name, lat, lng)"""
    return min(locations, key=lambda loc: distance_between(lat, lng, loc[1], loc[2]))


# first_name/last_name/email always together — should be a Contact class
def send_welcome(first_name, last_name, email):
    full_name = f"{first_name} {last_name}"
    print(f"Sending welcome to {full_name} at {email}")


def send_invoice(first_name, last_name, email, amount):
    full_name = f"{first_name} {last_name}"
    print(f"Invoice for {full_name} ({email}): ${amount:.2f}")


def update_contact(first_name, last_name, email, new_email):
    print(f"Updating {first_name} {last_name}: {email} -> {new_email}")
