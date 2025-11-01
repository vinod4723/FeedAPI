from fastapi import FastAPI
from app.api.routes import router as api_router
from app.api.employee import router as emp_router
from app.db.database import Base, engine
from app.db.models import Employee
app = FastAPI(title="Backend Automation API")


print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created")
# include all API routes
app.include_router(api_router, prefix="/api")
app.include_router(emp_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend Automation API is running!"}
