"""Clean code: order processing with clear responsibilities and no smells."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TaxRegion(Enum):
    DEFAULT = 0.080
    CA = 0.0925
    TX = 0.0825
    NY = 0.08875


@dataclass
class LineItem:
    name: str
    price: float
    quantity: int

    def subtotal(self) -> float:
        return self.price * self.quantity


@dataclass
class Order:
    items: list[LineItem]
    state: Optional[str] = None
    email: Optional[str] = None

    def subtotal(self) -> float:
        return sum(item.subtotal() for item in self.items)


def discount_for(subtotal: float) -> float:
    if subtotal > 100:
        return 0.10
    if subtotal > 50:
        return 0.05
    return 0.0


def shipping_for(subtotal: float) -> float:
    if subtotal < 25:
        return 7.99
    if subtotal < 50:
        return 4.99
    return 0.0


def tax_rate_for(state: Optional[str]) -> float:
    try:
        return TaxRegion[state].value
    except KeyError:
        return TaxRegion.DEFAULT.value


@dataclass
class Receipt:
    items: list[LineItem]
    subtotal: float
    discount: float
    tax: float
    shipping: float

    @property
    def total(self) -> float:
        return self.subtotal + self.tax + self.shipping


def build_receipt(order: Order) -> Receipt:
    subtotal = order.subtotal()
    discount = subtotal * discount_for(subtotal)
    discounted = round(subtotal - discount, 2)
    tax = round(discounted * tax_rate_for(order.state), 2)
    shipping = shipping_for(discounted)
    return Receipt(
        items=order.items,
        subtotal=discounted,
        discount=round(discount, 2),
        tax=tax,
        shipping=shipping,
    )


class EmailService:
    def send_order_confirmation(self, receipt: Receipt, email: str) -> None:
        print(f"Sending confirmation to {email}: total ${receipt.total:.2f}")


def process_order(order: Order, email_service: EmailService) -> Receipt:
    receipt = build_receipt(order)
    if order.email:
        email_service.send_order_confirmation(receipt, order.email)
    return receipt
