"""Offline demonstration; no external services or credentials required."""
import argparse, json
from decimal import Decimal, InvalidOperation

def quote(amount):
    fee = (amount * Decimal("0.001")).quantize(Decimal("0.000001"))
    return {"mode": "mock quote; no bridge transaction", "source": "demo-chain-a",
            "destination": "demo-chain-b", "amount": str(amount), "fee": str(fee),
            "received": str(amount - fee), "asset": "DEMO", "fee_rule": "synthetic 0.1 percent"}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Synthetic bridge quote, no wallet/network required.")
    p.add_argument("--amount", default="100")
    a = p.parse_args()
    try: amount = Decimal(a.amount)
    except InvalidOperation: p.error("amount must be a number")
    if not amount.is_finite() or amount <= 0 or amount > Decimal('1e12'): p.error("amount must be positive, finite and at most 1e12")
    print(json.dumps(quote(amount), indent=2))
