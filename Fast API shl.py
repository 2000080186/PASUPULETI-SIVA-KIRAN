from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from transformers import pipeline
import json

# Initialize FastAPI app
app = FastAPI()

# Load spaCy NLP model for text processing
nlp = spacy.load('en_core_web_sm')

# Example: Using Hugging Face's Transformers to load a pre-trained question-answering model (you can also use GPT or similar models)
qa_pipeline = pipeline("question-answering")

# Example of a SHL catalog data (this would usually be fetched from a database or an external file)
shl_catalog = [
    {
        "assessment_name": "Java Development Skills Test",
        "url": "https://www.shl.com/solutions/products/java-developer-assessment",
        "remote_testing": "Yes",
        "adaptive_support": "Yes",
        "duration": "40 minutes",
        "test_type": "Skills Assessment"
    },
    {
        "assessment_name": "Python Developer Test",
        "url": "https://www.shl.com/solutions/products/python-developer-assessment",
        "remote_testing": "Yes",
        "adaptive_support": "No",
        "duration": "60 minutes",
        "test_type": "Skills Assessment"
    },
    {
        "assessment_name": "Cognitive Ability Test",
        "url": "https://www.shl.com/solutions/products/cognitive-ability-assessment",
        "remote_testing": "Yes",
        "adaptive_support": "Yes",
        "duration": "30 minutes",
        "test_type": "Cognitive Assessment"
    }
]

# Define request body model
class Query(BaseModel):
    query: str

# Endpoint for getting relevant assessments based on a query
@app.post("/get_assessments/")
async def get_assessments(query: Query):
    # Process the query using spaCy to extract entities (this can be expanded as needed)
    doc = nlp(query.query)

    # Here we can use NLP or a model to extract meaningful info (e.g., skills, role, duration)
    # For the sake of simplicity, we'll assume it extracts key words like "Java", "Python", etc.

    # Example of keyword extraction logic (you can enhance this)
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    
    # For simplicity, we're matching keywords with test names or types
    relevant_assessments = []
    for assessment in shl_catalog:
        if any(keyword.lower() in assessment["assessment_name"].lower() for keyword in keywords):
            relevant_assessments.append(assessment)
    
    # Return results in JSON format
    return {"recommendations": relevant_assessments}

