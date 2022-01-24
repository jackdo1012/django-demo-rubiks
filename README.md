## How to run

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8080
```

App is ready at http://localhost:8080

## API list

-   GET /api/rubiks - Get all rubiks
-   POST /api/rubiks - New rubiks with name, layers and brand
-   GET /api/rubiks/:id - Get rubik using id
-   DELETE /api/rubiks/:id - Delete rubik using id
