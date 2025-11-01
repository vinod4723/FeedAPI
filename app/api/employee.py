from fastapi import APIRouter, Depends
from flask import session
from sqlalchemy.orm import Session, Query
from app.services.employee_service import get_all_employees
from app.db.database import get_db
router = APIRouter()
'call the below method using query string as http://127.0.0.1:8000/api/getEmployees?emp_id=2'
@router.get("/getEmployees")
def get_employees(emp_id: int,db: Session = Depends(get_db)):
    employees = get_all_employees(db, emp_id)
    return employees

'call the below method as http://127.0.0.1:8000/api/getEmployees/2'
@router.get("/getEmployees/{emp_id}")
def get_employee(emp_id: int,db: Session = Depends(get_db)):
    employee = get_all_employees(db, emp_id)
    return employee

