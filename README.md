# Product Inventory Management System

## Introduction
This project is a Python-based Product Inventory Management System.
It calculates product prices, applies discounts and checks stock availability.

## Features
- Calculate total product price.
- Apply percentage discounts.
- Check product stock availability.
- Validate invalid inputs using ValueError.
- Record application events using Python logging.
- Test functions using pytest.
- Check code quality using Ruff.

## Technologies Used
- Python 3
- Pytest
- Ruff
- Python Logging

## Project Structure

product_inventory/
├── inventory.py
├── test_inventory.py
├── inventory.log
├── README.md
└── .gitignore

## macOS Setup Instructions

1. Clone the repository.
2. Open Terminal and navigate to the project folder.
3. Create a virtual environment:

python3 -m venv .venv

4. Activate the environment:

source .venv/bin/activate

5. Install dependencies:

python -m pip install pytest ruff

## Run the Application

python inventory.py

## Run Unit Tests

python -m pytest -v

## Run Ruff Checks

python -m ruff check .

## Format Python Files

python -m ruff format inventory.py test_inventory.py

## Logging

Application logs are stored in inventory.log.

To view logs:

cat inventory.log

## Testing

The project contains eight test cases covering:
- Total price calculation.
- Zero quantity.
- Negative price.
- Negative quantity.
- Discount calculation.
- Invalid discount.
- Available stock.
- Insufficient stock.

## Conclusion

The Product Inventory Management System demonstrates Python functions,
input validation, exception handling, unit testing, logging and code quality.
