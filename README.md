# Interesse – Automation with Playwright and FastAPI

Interesse is a technical project developed as part of a job interview test. The main objective is to automate a purchase flow on Amazon using tools such as Playwright for browser automation and FastAPI for handling parameters through a local endpoint.

# What does this project do?

The script performs a full automation of a shopping process on Amazon. The flow includes:

- Logging in with a provided username and password.
- Navigating to the 55-inch TVs section.
- Adding the first displayed item to the shopping cart.
- Simulating the checkout process.

This execution is triggered through a local API built with FastAPI, which receives the necessary parameters (headless mode, username, and password) before launching the test.

# Project structure

INTERESSE/
│
├── API.py                 # FastAPI endpoint definition
├── requirements.txt       # Project dependencies
├── venv/                  # Python virtual environment
├── .gitignore
│
└── main/
    ├── test/
    │   ├── amazon_test.py     # Main test script
    │   ├── base_test.py       # Helper functions for the test
    │   ├── locators.py        # Element selectors for Amazon
    │   └── __init__.py

# Installation and setup

1. Clone the repository

git clone <repository-url>
cd INTERESSE

2. Activate the virtual environment

In PowerShell (Windows):
.\venv\Scripts\Activate.ps1

3. Install project dependencies

pip install -r requirements.txt

# 4. Install Playwright browsers

playwright install

# Running the project

1. Start the API

First, run the API that serves as the test's entry point:

uvicorn API:app --reload

This will start a server at `http://localhost:8000`, exposing a `/login` endpoint to receive test parameters.

# 2. Run the automation script

In a new terminal (with the virtual environment activated), run:

python -m main.test.amazon_test

This command will execute the full test. Make sure the API is running beforehand.

# Additional notes

- The project requires an internet connection and valid Amazon credentials to log in successfully.
- You can control whether the execution runs in headless mode by sending the appropriate data to the endpoint.
- This project is meant for demonstration purposes, showcasing end-to-end automation testing, API consumption, and the integration of Playwright with FastAPI.
