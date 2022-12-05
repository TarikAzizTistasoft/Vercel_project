from fastapi import FastAPI
from seoanalyzer import analyze
@app.get("/", tags=["Root"])
async def read_root():
  return { 
    "message": "Welcome to my notes application, use the /docs route to proceed."
   }