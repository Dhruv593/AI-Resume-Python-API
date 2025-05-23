# Resume Job API

A FastAPI-based API for managing resumes and jobs with MongoDB integration.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following content:
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/mydatabase
DB_NAME=your_database_name
```

## Running the Application

Start the server with:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Available Endpoints

- `GET /api/v1/resumes` - Get all resumes
- `GET /api/v1/jobs` - Get all jobs

## Response Format

All endpoints return data in the following format:
```json
{
  "success": true,
  "message": "Data fetched successfully",
  "data": [ /* list of documents */ ]
}
``` 