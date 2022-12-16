## Used Technologies/Concepts

### Backend

- Python
- Flask
- RESTful

### Database

- PostgreSQL

### Frontend

- React

---

## Setup Instructions

We used latest Python version 3.10

### Backend(Flask)

1. Create a python virtual environment and activate it. Later change directory to flask-apis
   ```
   cd Auction
   python -m venv <ENV_PATH> #flask_env:(ENV_PATH)
   source <ENV_PATH>/bin/activate
   cd flask-apis
   ```
2. Install dependencies
   `pip install -r requrements.txt`
3. Do neccesary changes in **config.py**(i.e DB connects: Use username(Student) and Password (Alchemy DB password) )

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

Now your backend is running on port 8089(We can change it in "app.py" if required). To access admin page, visit http://localhost:8089/admin ( Admin)

### Frontend(React)

1. Prerequisites: Make sure you have node installed in your machine
   node --version (Node: 14\*)

2. Install node module dependencies
   ```
   cd react-view
   npm install
   ```
3. Start react app

   ```
   npm start

   **Note:** use http://localhost:3000/ (front end)
   ```

4. Now, your react app will be up and running on 3000 port
   ** Note:** Make sure go the path ( /Auction/react-view/src/service requests) and make server port update to match with backend running port.

**Note:**
http://localhost:8089/admin ( Admin)
http://localhost:3000/ (front end)

