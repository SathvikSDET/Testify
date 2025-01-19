# Testify

**Testify** is an automated testing framework designed for functional, regression, and end-to-end testing of web applications. It leverages Selenium WebDriver for browser automation and includes a modular structure for easy test case management.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Browser Compatibility**: Supports Chrome, Firefox, Safari, and Edge.
- **Remote Execution**: Grid support for parallel and distributed test execution.
- **Headless Mode**: Option to run tests without opening the browser UI.
- **Custom Configuration**: Centralized configuration for managing environments, browser options, and URLs.
- **Modular Design**: Base classes and reusable components for efficient test case creation.

---

## Project Structure

```plaintext
Testify/
├── pages/                # Page Object Model classes
├── tests/                # Test scripts
├── utils/                # Utilities (e.g., configuration, helpers)
├── reports/              # Test reports (generated after execution)
├── driverFactory.py      # WebDriver factory for browser initialization
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── config.ini            # Configuration file
├── .gitignore            # Git ignore rules
└── .venv/                # Virtual environment (optional, not included in Git)
```

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- WebDriver binaries for Chrome, Firefox, or other browsers.
- (Optional) Selenium Grid setup for remote execution.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/testify.git
   cd testify
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For Linux/Mac
   .venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add the required WebDriver executables (e.g., `chromedriver`) to your system PATH.

---

## Configuration

The `config.ini` file is used to manage environment-specific settings, browser preferences, and Grid configurations.

### Example `config.ini`:

```ini
[Grid]
Grid = False
browser = chrome
headless = True
remote_url = http://localhost:4444/wd/hub

[URL]
baseURL = https://your-app-url.com
```

- **Grid**: Set to `True` to use Selenium Grid; otherwise, tests will run locally.
- **Browser**: Specify the browser (`chrome`, `firefox`, etc.).
- **Headless**: Run tests in headless mode if `True`.
- **Remote URL**: Selenium Grid URL for remote execution.

---

## Running Tests

### Run All Tests

To execute all test scripts in the project:

```bash
pytest tests/
```

### Run Specific Test File

```bash
pytest tests/test_login.py
```

### Generate Reports

Use the `pytest-html` plugin for detailed HTML reports:

```bash
pytest tests/ --html=reports/report.html
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For queries or feedback, reach out to the project maintainer at [your-email@example.com].

