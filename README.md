1. Install Python (Use Latest Stable)

Visit: https://www.python.org/downloads/

As of 2025, Python 3.12 or 3.13 is recommended.

On Windows: ✅ Check “Add Python to PATH” during install.

Verify:
```
python --version
```
### create a folder and open that folder into editor.
### create folder structure as below.
```
FeedAPI/
│
├── .venv/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entrypoint
│   ├── api/
│   │   └── routes.py
│   ├── db/
        └── database.py
│   │   └── models.py
│   ├── services/
│   │  
│   ├── utils/
│       └── helpers.py
│
├── automation/
│
├── tests/
│   └── test_api.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```
### Create Requirements.txt file and add below libraries
````
fastapi
sqlalchemy
pyodbc
requests
httpx
schedule
uvicorn[standard]
pydantic
````
### Run below command for test project
```
pip install pytest pytest-cov
```
### Install sql alchemy to connect with sql server database.
```
pip install sqlalchemy pyodbc python-dotenv
```
### Write the code to configure the API
```
-- add the below code inAPI class
from fastapi import APIRouter, Depends
router = APIRouter()

@router.get("/getEmployees/{emp_id}")
def get_employee(emp_id: int,db: Session = Depends(get_db)):
    employee = get_all_employees(db, emp_id)
    return employee
    
-- register above class into main.py
from fastapi import FastAPI
from app.api.routes import router as api_router

app.include_router(api_router, prefix="/api")

'Default route '
@app.get("/")
def root():
    return {"message": "Backend Automation API is running!"}
```

### now to run the application , execute the below command
```
uvicorn app.main:app --reload  
```
