# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import resumes, jobs
from .db.connection import connect_to_mongo, close_mongo_connection

app = FastAPI(
    title="Resume Job API",
    description="API for managing resumes and jobs",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(resumes.router, prefix="/api/v1", tags=["resumes"])
app.include_router(jobs.router, prefix="/api/v1", tags=["jobs"])

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {
        "message": "Welcome to Resume Job API",
        "version": "1.0.0",
        "docs_url": "/docs"
    } 