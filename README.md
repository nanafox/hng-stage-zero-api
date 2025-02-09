# HNG Stage Zero Task

## Task Description

Develop a public API that returns the following information in JSON format:

1. **Your registered email address** (used to register on the HNG12 Slack workspace).
2. **The current datetime** as an ISO 8601 formatted timestamp.
3. **The GitHub URL** of the project's codebase.

## API Specification

- Documentation URL:
[https://nanafox-hng-stage-zero-6049d997f8d2.herokuapp.com/docs](https://nanafox-hng-stage-zero-6049d997f8d2.herokuapp.com/docs)
- Swagger (Interactive Docs) URL:
[https://nanafox-hng-stage-zero-6049d997f8d2.herokuapp.com/swagger-doc](https://nanafox-hng-stage-zero-6049d997f8d2.herokuapp.com/swagger-doc)
- Endpoint: [https://nanafox-hng-stage-zero-6049d997f8d2.herokuapp.com](https://nanafox-hng-stage-zero-6049d997f8d2.herokuapp.com)
- Response:

    ```json
    {
        "email": "myemail@example.com",
        "current_datetime": "2025-01-01T10:00:00Z",
        "github_url": "https://github.com/nanafox/hng-stage-zero-api"
    }
    ```

## Development

To run this project locally, follow the steps below:

1. Clone the repository:

    ```bash
    git clone https://github.com/nanafox/hng-stage-zero-api.git
    ```

2. Change directory:

    ```bash
    cd hng-stage-zero-api
    ```

3. Install dependencies (it is recommended to create a virtual environment):

    ```bash
    pip install -r requirements.txt
    ```

4. Set the required variables in the `env` file. See `.env.template` for how to
   set it up.

5. Run the application:

    ```bash
    fastapi dev app/main.py
    ```

6. Access the swagger documentation at [http://localhost:8000/swagger-doc](http://localhost:8000/swagger-doc)

7. API Documentation is available at:
   [http://localhost:8000/docs](http://localhost:8000/docs)

## Language Stack

Backlink: [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

- Python
- FastAPI
