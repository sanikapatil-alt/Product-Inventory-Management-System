import logging

logging.basicConfig(
    filename="Application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def calculate_total_price(price, quantity):
    if price < 0:
        logger.error("Price cannot be negative")
        raise ValueError("Price cannot be negative")

    if quantity < 0:
        logger.error("Quantity cannot be negative")
        raise ValueError("Quantity cannot be negative")

    total = price * quantity
    logger.info("Total price calculated: %s", total)
    return total


def apply_discount(total, discount_percent):
    if total < 0:
        logger.error("Total cannot be negative")
        raise ValueError("Total cannot be negative")

    if not 0 <= discount_percent <= 100:
        logger.error("Invalid discount percentage")
        raise ValueError("Discount must be between 0 and 100")

    discounted_amount = total - (total * discount_percent / 100)
    logger.info("Discount applied: %s", discounted_amount)
    return discounted_amount


def check_stock(available_stock, requested_quantity):
    if available_stock < 0 or requested_quantity < 0:
        logger.error("Stock quantities cannot be negative")
        raise ValueError("Stock quantities cannot be negative")

    if requested_quantity <= available_stock:
        logger.info("Stock available")
        return True

    logger.warning("Insufficient stock")
    return False


if __name__ == "__main__":
    price = calculate_total_price(500, 3)
    print("Total price:", price)

    discounted_price = apply_discount(price, 10)
    print("Price after discount:", discounted_price)

    stock_status = check_stock(20, 5)
    print("Stock available:", stock_status)
