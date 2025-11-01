from sqlalchemy.orm import Session
from app.db import models

def get_all_employees(db: Session, emp_id:int=0):
    """Fetch all employees from the database."""
    employees = []
    if emp_id >0:
        employees = db.query(models.Employee).filter(models.Employee.id == emp_id).all()
    else:
        employees = db.query(models.Employee).all()

    return employees





