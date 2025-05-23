# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException
from ...db.connection import db
from bson import ObjectId
import base64

router = APIRouter()

@router.get("/resumes")
async def get_resumes():
    try:
        # Fetch all documents from resumes collection
        cursor = db.db.resumes.find()
        resumes = await cursor.to_list(length=None)
        
        # Process each resume document
        processed_resumes = []
        for resume in resumes:
            # Create a new dict for the processed resume
            processed_resume = {}
            
            # Process each field
            for key, value in resume.items():
                if key == '_id':
                    processed_resume[key] = str(value)
                elif isinstance(value, bytes):
                    # Convert binary data to base64 string
                    try:
                        processed_resume[key] = base64.b64encode(value).decode('ascii')
                    except:
                        processed_resume[key] = None
                else:
                    processed_resume[key] = value
            
            processed_resumes.append(processed_resume)
        
        return {
            "success": True,
            "message": "Resumes fetched successfully",
            "data": processed_resumes
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching resumes: {str(e)}"
        ) 