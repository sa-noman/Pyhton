from dataclasses import dataclass
from datetime import datetime

@dataclass
class Receipt:
    item: str
    quantity: int
    unit_price: float

    @property
    def total(self):
        return self.quantity * self.unit_price

def render_receipt(receipt):
    return (
        f"PAYMENT RECEIPT\n"
        f"Date: {datetime.now():%Y-%m-%d %H:%M}\n"
        f"Item: {receipt.item}\n"
        f"Quantity: {receipt.quantity}\n"
        f"Unit price: {receipt.unit_price:.2f}\n"
        f"Total: {receipt.total:.2f}\n"
    )

if __name__ == "__main__":
    receipt = Receipt(input("Item: "), int(input("Quantity: ")), float(input("Unit price: ")))
    text = render_receipt(receipt)
    print(text)
    with open("receipt.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
