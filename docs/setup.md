Setup Virtual Environment & Activate
    python3 -m venv venv
    source venv/bin/activate

Install the dependencies
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

    If you don’t have a requirements.txt yet, generate one:
        python -m pip freeze > requirements.txt

Run the application
    uvicorn app.main:app --reload

