"""Code smell: Shotgun Surgery — one logical change requires edits in many places.

Scenario: adding a new payment method (e.g. "crypto") requires touching all of these
unrelated functions scattered across the module.
"""


SUPPORTED_METHODS = ["credit_card", "paypal", "bank_transfer"]  # add here


def validate_payment_method(method):
    if method not in ["credit_card", "paypal", "bank_transfer"]:  # and here
        raise ValueError(f"Unsupported payment method: {method}")


def get_payment_fee(method, amount):
    if method == "credit_card":
        return amount * 0.029 + 0.30
    elif method == "paypal":
        return amount * 0.034 + 0.30
    elif method == "bank_transfer":
        return 0.25
    else:
        return 0  # and handle here


def get_payment_processing_time(method):
    times = {
        "credit_card": "instant",
        "paypal": "instant",
        "bank_transfer": "2-3 business days",
        # add new method here too
    }
    return times.get(method, "unknown")


def render_payment_icon(method):
    icons = {
        "credit_card": "💳",
        "paypal": "🅿",
        "bank_transfer": "🏦",
        # and here
    }
    return icons.get(method, "❓")


def get_payment_instructions(method):
    if method == "credit_card":
        return "Enter your card number, expiry, and CVV."
    elif method == "paypal":
        return "You will be redirected to PayPal to complete your payment."
    elif method == "bank_transfer":
        return "Transfer funds to account number 12345678, sort code 00-00-00."
    # and here


def log_payment_attempt(method, amount, success):
    # Each method has its own logging category — add new one here too
    categories = {
        "credit_card": "card_payments",
        "paypal": "paypal_payments",
        "bank_transfer": "ach_payments",
    }
    category = categories.get(method, "other_payments")
    status = "SUCCESS" if success else "FAILURE"
    print(f"[{category}] {status}: ${amount:.2f} via {method}")
