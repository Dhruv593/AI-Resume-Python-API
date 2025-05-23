# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException
from ...db.connection import db
from bson import ObjectId
import base64

router = APIRouter()

@router.get("/jobs")
async def get_jobs():
    try:
        # Fetch all documents from jobs collection
        cursor = db.db.jobs.find()
        jobs = await cursor.to_list(length=None)
        
        # Process each job document
        processed_jobs = []
        for job in jobs:
            # Create a new dict for the processed job
            processed_job = {}
            
            # Process each field
            for key, value in job.items():
                if key == '_id':
                    processed_job[key] = str(value)
                elif isinstance(value, bytes):
                    # Convert binary data to base64 string
                    try:
                        processed_job[key] = base64.b64encode(value).decode('ascii')
                    except:
                        processed_job[key] = None
                else:
                    processed_job[key] = value
            
            processed_jobs.append(processed_job)
        
        return {
            "success": True,
            "message": "Jobs fetched successfully",
            "data": processed_jobs
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching jobs: {str(e)}"
        ) 