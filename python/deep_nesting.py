"""Code smell: Deep Nesting — arrow-shaped code that's hard to follow."""


def process_transaction(transaction):
    if transaction:
        if transaction.get("amount"):
            if transaction["amount"] > 0:
                if transaction.get("user"):
                    user = transaction["user"]
                    if user.get("active"):
                        if not user.get("blocked"):
                            if user.get("balance") is not None:
                                if user["balance"] >= transaction["amount"]:
                                    if transaction.get("merchant"):
                                        merchant = transaction["merchant"]
                                        if merchant.get("active"):
                                            if not merchant.get("flagged"):
                                                user["balance"] -= transaction["amount"]
                                                transaction["status"] = "approved"
                                                return transaction
                                            else:
                                                transaction["status"] = "rejected_flagged_merchant"
                                        else:
                                            transaction["status"] = "rejected_inactive_merchant"
                                    else:
                                        transaction["status"] = "rejected_no_merchant"
                                else:
                                    transaction["status"] = "rejected_insufficient_funds"
                            else:
                                transaction["status"] = "rejected_no_balance"
                        else:
                            transaction["status"] = "rejected_blocked_user"
                    else:
                        transaction["status"] = "rejected_inactive_user"
                else:
                    transaction["status"] = "rejected_no_user"
            else:
                transaction["status"] = "rejected_invalid_amount"
        else:
            transaction["status"] = "rejected_missing_amount"
    return transaction


def find_discount(user, product, promo_code):
    discount = 0
    if user:
        if user.get("membership") == "premium":
            if product:
                if product.get("category") == "electronics":
                    if promo_code:
                        if promo_code == "SAVE20":
                            discount = 0.20
                        elif promo_code == "SAVE10":
                            discount = 0.10
                    else:
                        discount = 0.05
                elif product.get("category") == "clothing":
                    if promo_code == "FASHION15":
                        discount = 0.15
            else:
                discount = 0.03
        elif user.get("membership") == "basic":
            if promo_code == "WELCOME10":
                discount = 0.10
    return discount
