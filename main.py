from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Dict, List

app = FastAPI(
    title="Production API Bootstrap",
    description="High-performance starter template for secure enterprise backends.",
    version="1.0.0"
)

# In-memory database simulation using highly-efficient O(1) dictionary lookups
USER_DB_MOCK: Dict[str, Dict[str, Any]] = {}

class UserCreateSchema(BaseModel):
    username: str
    email: str
    is_active: bool = True

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Welcome to the Production API Bootstrap. System status: Operational."}

@app.post("/api/v1/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreateSchema):
    if user.email in USER_DB_MOCK:
        raise HTTPException(status_code=400, detail="Resource already exists in records.")
    
    USER_DB_MOCK[user.email] = user.model_dump()
    return {"status": "success", "data": USER_DB_MOCK[user.email]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
  
