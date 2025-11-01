from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class Employee(Base):
    __tablename__ = "Employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    department = Column(String(50))
    email = Column(String(100))

class Department(Base):
    __tablename__ = "Departments"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(50))


class EmpDepartments(Base):
    __tablename__ = "EmpDepartments"

    id = Column(Integer, primary_key=True, index=True)
    empId = Column(Integer, ForeignKey('Employees.id'))
    deptId = Column(Integer, ForeignKey('Departments.id'))

