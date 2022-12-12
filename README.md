# Flask Documentation
used python 3.10
- install dependencies
- change db connection at config.py


```
Open python shell and run the following code to create tables defined in models.py

from app import *
app = create_app()
with app.app_context():
    db.create_all()
    db.drop_all()
```
