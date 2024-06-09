# Password Strength Checker

A web tool to check the strength of a password and verify if it has been exposed in known data leaks. The tool allows users to select between different leak-checking APIs and provide their own API keys if desired.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Description

This project is a web-based Password Strength Checker developed using Flask and Python. It allows users to input a password and check its strength. Additionally, the tool verifies if the password has been exposed in known data leaks using the Have I Been Pwned API by default. Users can also choose to use a custom API for leak checks by providing their API key.

## Features

- **Password Strength Check**: Analyzes the complexity of the password based on length, uppercase letters, lowercase letters, digits, and special characters.
- **Leak Check using Have I Been Pwned API**: Checks if the password has been exposed in known data breaches.
- **Custom Leak Check API**: Allows users to use a different leak-checking API by providing their own API key.

## Prerequisites

Ensure the following packages are installed on your system:

- Python 3
- Pip
- Virtual Environment (optional but recommended)
- Git

## Installation

1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd password_checker
# PW_checker

2. Create and activate a virtual environment (optional but recommended):
    virtualenv venv
    source venv/bin/activate

4. Install the dependencies:
     pip install -r requirements.txt
   

## Usage
1. Start the Flask app:
     python run.py

2. Open your web browser and navigate to http://127.0.0.1:5000/

3. Enter a password you want to check, select if you want to use a custom API, and provide the API key if needed.

4. View the results for password strength and leak check on the page.


## Project Structure
password_checker/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       └── index.html
│
├── checker/
│   ├── __init__.py
│   ├── strength.py
│   └── leak_check.py
│
├── tests/
│   ├── __init__.py
│
├── run.py
└── requirements.txt


## Contributing
Contributions are welcome! Please create an issue before making changes and open a pull request for your changes.
