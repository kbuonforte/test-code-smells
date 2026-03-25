"""Code smell: Primitive Obsession — using raw primitives instead of domain objects."""


def create_user(first_name, last_name, email, street, city, state, zip_code, country,
                card_number, card_expiry, card_cvv, card_holder):
    """Too many primitive parameters that belong in structured types."""
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "street": street,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "country": country,
        "card_number": card_number,
        "card_expiry": card_expiry,
        "card_cvv": card_cvv,
        "card_holder": card_holder,
    }


def format_address(street, city, state, zip_code, country):
    return f"{street}, {city}, {state} {zip_code}, {country}"


def is_valid_address(street, city, state, zip_code, country):
    return all([street, city, state, zip_code, country])


def ship_package(street, city, state, zip_code, country, weight, width, height, depth):
    """Address fields repeated everywhere instead of an Address type."""
    volume = width * height * depth
    print(f"Shipping {weight}kg ({volume}cm³) to {city}, {state}")


def calculate_shipping_cost(weight, width, height, depth, street, city, state, zip_code, country):
    volume = width * height * depth
    base = 5.0
    if country != "US":
        base += 15.0
    return base + (weight * 0.5) + (volume * 0.001)


# Magic numbers scattered everywhere instead of named constants
def score_applicant(age, income, credit_score, years_employed):
    score = 0
    if age >= 18 and age <= 65:
        score += 10
    if income > 50000:
        score += 20
    elif income > 30000:
        score += 10
    if credit_score > 750:
        score += 30
    elif credit_score > 650:
        score += 15
    elif credit_score < 580:
        score -= 20
    if years_employed > 5:
        score += 15
    elif years_employed > 2:
        score += 8
    return score >= 35
