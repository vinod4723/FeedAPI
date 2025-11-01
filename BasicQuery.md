⚙️ 1️⃣ 
### Basic Query — Fetch All Rows
def get_all_employees(db: Session):
    return db.query(Employee).all()

### Equivalent SQL:

SELECT * FROM Employees;

⚙️ 2️⃣ 
### Fetch One Record by ID
def get_employee_by_id(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

### Equivalent SQL:

SELECT TOP 1 * FROM Employees WHERE id = @emp_id;

⚙️ 3️⃣ 
### Filter by Column Values
def get_employees_by_department(db: Session, department: str):
    return db.query(Employee).filter(Employee.department_id == department).all()

### Use multiple filters:

db.query(Employee).filter(
    Employee.department_id == 2,
    Employee.email.like("%example.com")
).all()

### Equivalent SQL:

SELECT * FROM Employees
WHERE department_id = 2 AND email LIKE '%example.com';

⚙️ 4️⃣ 
### Using and_, or_, and not_ for Complex Conditions from sqlalchemy import and_, or_, not_

db.query(Employee).filter(
    or_(
        Employee.department_id == 2,
        Employee.name.like("A%")
    ),
    not_(Employee.email.like("%@test.com"))
).all()

### Equivalent SQL:

SELECT * FROM Employees
WHERE (department_id = 2 OR name LIKE 'A%')
AND email NOT LIKE '%@test.com';

⚙️ 5️⃣
### Order By (Ascending / Descending)
db.query(Employee).order_by(Employee.name.asc()).all()
db.query(Employee).order_by(Employee.id.desc()).all()

### Equivalent SQL:

SELECT * FROM Employees ORDER BY name ASC;
SELECT * FROM Employees ORDER BY id DESC;

⚙️ 6️⃣
### Limit and Offset (Pagination)
db.query(Employee).limit(10).offset(20).all()

### Equivalent SQL:
SELECT * FROM Employees ORDER BY id OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;

⚙️ 7️⃣ 
### Count / Aggregate Functions 
from sqlalchemy import func
total = db.query(func.count(Employee.id)).scalar()
print(total)

max_id = db.query(func.max(Employee.id)).scalar()

### Equivalent SQL:

SELECT COUNT(id) FROM Employees;
SELECT MAX(id) FROM Employees;

⚙️ 8️⃣
### Group By + Having
from sqlalchemy import func

result = (
    db.query(Employee.department_id, func.count(Employee.id).label("total"))
    .group_by(Employee.department_id)
    .having(func.count(Employee.id) > 5)
    .all()
)

### Equivalent SQL:

SELECT department_id, COUNT(id) AS total
FROM Employees
GROUP BY department_id
HAVING COUNT(id) > 5;

⚙️ 9️⃣
### Join Queries (Employee + Department)
result = (
    db.query(Employee.name, Department.name.label("department"))
    .join(Department, Employee.department_id == Department.id)
    .all()
)

### Equivalent SQL:

SELECT e.name, d.name AS department
FROM Employees e
JOIN Departments d ON e.department_id = d.id;

#### You can also use .outerjoin() for left joins.

⚙️ 🔟 
### Distinct and In/Not In
### Distinct
db.query(Employee.department_id).distinct().all()

### IN clause
db.query(Employee).filter(Employee.id.in_([1, 2, 3])).all()

### NOT IN
db.query(Employee).filter(~Employee.id.in_([5, 6])).all()


### Equivalent SQL:

SELECT DISTINCT department_id FROM Employees;
SELECT * FROM Employees WHERE id IN (1, 2, 3);
SELECT * FROM Employees WHERE id NOT IN (5, 6);

⚙️ 11️⃣
### Using Raw SQL Queries (When Needed)
result = db.execute("SELECT TOP 5 * FROM Employees WHERE department_id = :dep_id", {"dep_id": 2})
rows = result.fetchall()

### Or using SQLAlchemy Core:

from sqlalchemy import text
result = db.execute(text("SELECT * FROM Employees WHERE department_id=:dep_id"), {"dep_id": 2})

⚙️ 12️⃣
### Combine Multiple Tables in ORM Objects
### You can use relationships directly:

employees = db.query(Employee).join(Employee.department).all()
for emp in employees:
    print(emp.name, emp.department.name)

⚙️ 13️⃣
### Dynamic Filtering Example (Optional)
### You can apply filters dynamically using Python logic:

query = db.query(Employee)
if department:
    query = query.filter(Employee.department_id == department)
if name:
    query = query.filter(Employee.name.like(f"%{name}%"))
if email:
    query = query.filter(Employee.email.like(f"%{email}%"))
result = query.all()
