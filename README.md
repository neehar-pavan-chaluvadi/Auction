## Used Technologies/Concepts
### Backend
- Python
- Flask
- RESTful

### Database
- PostgreSQL
### Frontend
- React
----------------

## Setup Instructions
   We used latest Python version 3.10
### Backend(Flask)
1. Create a python virtual environment and activate it. Later change directory to flask-apis
    ```
    python -m venv <ENV_PATH>
    source <ENV_PATH>/bin/activate
    cd flask-apis
    ```
2. Install dependencies
    `pip install -r requrements.txt`
3. Do neccesary changes in **config.py**(i.e DB connects)
4. Start backend 
    ```
    python app.py
    ```
    Output should be some thing as below
    ![image](https://user-images.githubusercontent.com/120152444/207415644-64eba568-d002-49ca-98ef-46a31e157756.png)

**Note:** Follow the steps below if you're just getting started

    After step-3, In order to create tables in the database, we must first create those defined in models.py.
    Open the Python shell and execute the following code.
    ```
    >>> from app import *
    >>> app = create_app()
    >>> with app.app_context():
            db.create_all()
            #db.drop_all() (if you wanted to drop tables we can run this line)
    ```
Now your backend is running on port 8080(We can change it in "app.py" if required). To access admin page, visite http://localhost:8080/admin

### Frontend(React)
1. Prerequisites: Make sure you have node installed in your machine
2. Install node module dependencies
    ```
    cd react-view
    npm install
    ```
3. Start react app
    ```
    npm start
    ```
4. Now, your react app will be up and running on 3000 port
