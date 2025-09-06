# My Flask CI/CD Project

A simple Flask application that demonstrates a fully automated Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub and Render.

## Overview

This project serves as a practical example of DevOps principles. The workflow is as follows:

1.  A developer pushes code to the `main` branch on GitHub.
2.  Render automatically detects the new commit.
3.  The build process begins, which includes:
    * Installing Python dependencies from `requirements.txt`.
    * Running automated tests with `pytest` to ensure all features are working as expected.
4.  If the tests pass, the new version of the application is automatically deployed to production.

This process ensures that only tested and working code is deployed, reducing the risk of bugs and errors.

## Technologies Used

* **Flask**: A lightweight Python web framework.
* **Gunicorn**: A Python WSGI HTTP server for production.
* **pytest**: A testing framework for Python.
* **Render**: A cloud platform for web services, databases, and more.
* **GitHub**: For version control and triggering the CI/CD pipeline.

## Getting Started

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git

### Local Development

1.  Clone the repository:
    `git clone https://github.com/wilson7777777/my-flask-ci-cd-project.git`
    `cd my-flask-ci-cd-project`

2.  Create a virtual environment:
    `python -m venv .venv`
    `source .venv/bin/activate`  (on macOS/Linux)
    `.\.venv\Scripts\activate`    (on Windows)

3.  Install dependencies:
    `pip install -r requirements.txt`

4.  Run the application:
    `gunicorn app:app`

The application will be available at `http://localhost:8000`.

## CI/CD Pipeline Configuration

The build and deploy process is configured on Render. The build command `pip install -r requirements.txt && python -m pytest` is used to run tests before deployment.
