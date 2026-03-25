"""Clean code: payment methods via polymorphism instead of if-elif chains."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PaymentResult:
    success: bool
    fee: float
    processing_time: str
    message: str


class PaymentMethod(ABC):
    @abstractmethod
    def fee(self, amount: float) -> float: ...

    @abstractmethod
    def processing_time(self) -> str: ...

    @abstractmethod
    def instructions(self) -> str: ...

    def process(self, amount: float) -> PaymentResult:
        fee = self.fee(amount)
        return PaymentResult(
            success=True,
            fee=fee,
            processing_time=self.processing_time(),
            message=f"Charged ${amount + fee:.2f} (includes ${fee:.2f} fee)",
        )


class CreditCard(PaymentMethod):
    def fee(self, amount: float) -> float:
        return round(amount * 0.029 + 0.30, 2)

    def processing_time(self) -> str:
        return "instant"

    def instructions(self) -> str:
        return "Enter your card number, expiry, and CVV."


class PayPal(PaymentMethod):
    def fee(self, amount: float) -> float:
        return round(amount * 0.034 + 0.30, 2)

    def processing_time(self) -> str:
        return "instant"

    def instructions(self) -> str:
        return "You will be redirected to PayPal to complete your payment."


class BankTransfer(PaymentMethod):
    FIXED_FEE = 0.25

    def fee(self, amount: float) -> float:
        return self.FIXED_FEE

    def processing_time(self) -> str:
        return "2-3 business days"

    def instructions(self) -> str:
        return "Transfer funds to account number 12345678, sort code 00-00-00."


PAYMENT_METHODS: dict[str, PaymentMethod] = {
    "credit_card": CreditCard(),
    "paypal": PayPal(),
    "bank_transfer": BankTransfer(),
}


def get_payment_method(name: str) -> PaymentMethod:
    method = PAYMENT_METHODS.get(name)
    if method is None:
        supported = ", ".join(PAYMENT_METHODS)
        raise ValueError(f"Unknown payment method '{name}'. Supported: {supported}")
    return method
