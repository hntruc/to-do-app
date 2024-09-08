# TodoApp

A simple todo application.

## Features

- Create, update, and delete notes

## Technologies Used

- FASTAPI
- Streamlit
- PostgresQL

## Getting Started

1. Install Docker on your machine if you haven't already.

2. Clone the repository:

    ```bash
    git clone https://github.com/hntruc/to-do-app
    ```

3. Navigate to the project directory:

    ```bash
    cd todoapp_backend
    ```

4. Create a virtual environment and activate it, initialize a new Poetry project (if you don't have a pyproject.toml file yet)::

    ```bash
    poetry init
    ```

5. Install the required dependencies:

    ```bash
    poetry install
    ```

6. Start the PostgreSQL database container:

    ```bash
    docker-compose up -d
    ```

7. Start the FASTapi backend server:

    ```bash
    poetry run python -m todoapp_backend.main
    ```

8. In a separate terminal, navigate to the project directory:

    ```bash
    cd todoapp_frontend
    ```

8. Then, start the Streamlit frontend:

    ```bash
    poetry run streamlit run streamlit_app.py
    ```

9. Open your browser and navigate to `http://localhost:8501` to access the Todoapp.

10. Use the Todoapp to create, update, and delete tasks, mark tasks as complete.

11. When you're done, stop the containers:

    ```bash
    docker-compose down
    ```

That's it! You have successfully implemented the Todoapp using FASTapi, Streamlit, Postgres, and Docker.

## Running Tests

To run the tests, use the following command:

    ```bash
    poetry run pytest test_crud.py
    ```

## Usage

- Create a new task by entering a title and optional description.
- Update a task by clicking on it and modifying the details.
- Mark a task as complete by checking the checkbox next to it.
- Delete a task by clicking on the delete button.

## License

This project is a pet project.