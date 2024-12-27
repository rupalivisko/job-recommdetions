
#Real code
# import streamlit as st
# import pickle
# import pandas as pd
# # company	employmenttype_jobstatus	jobdescription	jobid	joblocation_address	jobtitle	skills	job_tags	job_tags1
# #recommend function
# def recommend(movie):
#         movie_index = data[data['jobtitle'] == movie].index[0]
#         distances = similarity[movie_index]
#         movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

#         recommend_movies = []
#         for i in movie_list:
#             recommend_movies.append(data.iloc[i[0]][['company','employmenttype_jobstatus','joblocation_address','jobtitle','skills']])

#         return recommend_movies

    
# # Importing the dataset 
# Job_dict = pickle.load(open('Job_recom.pkl','rb'))
# data = pd.DataFrame(Job_dict)
# similarity = pickle.load(open('job_similiar.pkl','rb'))


# # Title of Page
# st.title('Jobs Recommendation System')

# select_movie_name = st.selectbox(
# "How would you like to be contacted?",
# data['jobtitle'].values)


# #Button
# if st.button('Recommend'):
#     recommendations = recommend(select_movie_name)
#     for i in recommendations:
#         st.write(i) 




#convert to json response 
# import streamlit as st
# import pickle
# import pandas as pd
# import json

# # recommend function
# def recommend(movie):
#     movie_index = data[data['jobtitle'] == movie].index[0]
    
#     distances = similarity[movie_index]

#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

#     recommend_jobs = []
#     for i in movie_list:
#         job_details = {
#             "company": data.iloc[i[0]]['company'],
#             "employment_type": data.iloc[i[0]]['employmenttype_jobstatus'],
#             "job_location": data.iloc[i[0]]['joblocation_address'],
#             "job_title": data.iloc[i[0]]['jobtitle'],
#             "skills": data.iloc[i[0]]['skills']
#         }
#         recommend_jobs.append(job_details)

#     return recommend_jobs

# # Importing the dataset
# Job_dict = pickle.load(open('Job_recom.pkl', 'rb'))
# data = pd.DataFrame(Job_dict)
# # print(data)
# similarity = pickle.load(open('job_similiar.pkl', 'rb'))
# # print(similarity)

# # Title of Page
# st.title('Jobs Recommendation System')

# # Select a job title
# select_movie_name = st.selectbox(
#     "Select a job title for recommendations:",
#     data['jobtitle'].values
# )

# # Button
# if st.button('Recommend'):
#     recommendations = recommend(select_movie_name)
    
#     # Display recommendations in Streamlit
#     for job in recommendations:
#         st.write(job)
    
#     # Output recommendations as JSON in the console
#     print(json.dumps(recommendations, indent=4))



#fastapi based 
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pickle
# import pandas as pd
# from typing import List

# # Load pre-trained data and similarity matrix
# Job_dict = pickle.load(open('Job_recom.pkl', 'rb'))
# data = pd.DataFrame(Job_dict)
# similarity = pickle.load(open('job_similiar.pkl', 'rb'))

# # Initialize FastAPI app
# app = FastAPI()

# # Pydantic model for response schema
# class JobRecommendation(BaseModel):
#     company: str
#     employment_type: str
#     job_location: str
#     job_title: str
#     skills: str

# # Function to recommend jobs
# def recommend(job_title: str) -> List[JobRecommendation]:
#     if job_title not in data['jobtitle'].values:
#         raise HTTPException(status_code=404, detail="Job title not found")
    
#     job_index = data[data['jobtitle'] == job_title].index[0]
#     distances = similarity[job_index]
#     job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

#     recommend_jobs = []
#     for i in job_list:
#         job_details = {
#             "company": data.iloc[i[0]]['company'],
#             "employment_type": data.iloc[i[0]]['employmenttype_jobstatus'],
#             "job_location": data.iloc[i[0]]['joblocation_address'],
#             "job_title": data.iloc[i[0]]['jobtitle'],
#             "skills": data.iloc[i[0]]['skills']
#         }
#         recommend_jobs.append(job_details)

#     return recommend_jobs

# # FastAPI route for job recommendations
# @app.get("/recommendations/", response_model=List[JobRecommendation])
# async def get_recommendations(job_title: str):
#     recommendations = recommend(job_title)
#     return recommendations



#postmen
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pickle
# import pandas as pd
# from typing import List

# # Load pre-trained data and similarity matrix
# Job_dict = pickle.load(open('Job_recom.pkl', 'rb'))
# data = pd.DataFrame(Job_dict)
# similarity = pickle.load(open('job_similiar.pkl', 'rb'))

# # Initialize FastAPI app
# app = FastAPI()

# # Pydantic model for input and response schema
# class JobRequest(BaseModel):
#     job_title: str

# class JobRecommendation(BaseModel):
#     company: str
#     employment_type: str
#     job_location: str
#     job_title: str
#     skills: str

# # Function to recommend jobs
# def recommend(job_title: str) -> List[JobRecommendation]:
#     if job_title not in data['jobtitle'].values:
#         raise HTTPException(status_code=404, detail="Job title not found")
    
#     job_index = data[data['jobtitle'] == job_title].index[0]
#     distances = similarity[job_index]
#     job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

#     recommend_jobs = []
#     for i in job_list:
#         job_details = {
#             "company": data.iloc[i[0]]['company'],
#             "employment_type": data.iloc[i[0]]['employmenttype_jobstatus'],
#             "job_location": data.iloc[i[0]]['joblocation_address'],
#             "job_title": data.iloc[i[0]]['jobtitle'],
#             "skills": data.iloc[i[0]]['skills']
#         }
#         recommend_jobs.append(job_details)

#     return recommend_jobs

# # FastAPI route for job recommendations (POST request with JSON body)
# @app.post("/recommendations/", response_model=List[JobRecommendation])
# async def get_recommendations(request: JobRequest):
#     recommendations = recommend(request.job_title)
#     return recommendations


from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from pydantic import BaseModel
import pickle
import pandas as pd
import json

# Load pre-trained data and similarity matrix
Job_dict = pickle.load(open('Job_recom.pkl', 'rb'))
data = pd.DataFrame(Job_dict)
similarity = pickle.load(open('job_similiar.pkl', 'rb'))

# Initialize FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/visko"
engine = create_engine(DATABASE_URL, echo=True)

# Create a sessionmaker instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Define the SQLAlchemy model for job recommendations
class JobRecommendationTable(Base):
    __tablename__ = 'job_recommendations'
    
    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String(255), index=True)
    recommended_jobs = Column(Text)  

# Create the table if it doesn't exist
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for input and output
class JobRequest(BaseModel):
    job_title: str

class JobRecommendationResponse(BaseModel):
    company: str
    employment_type: str
    job_location: str
    job_title: str
    skills: str

    class Config:
        from_attributes = True 

# Function to recommend jobs
def recommend(job_title: str) -> List[JobRecommendationResponse]:
    if job_title not in data['jobtitle'].values:
        raise HTTPException(status_code=404, detail=f"Job title '{job_title}' not found in the dataset.")
    
    job_index = data[data['jobtitle'] == job_title].index[0]
    distances = similarity[job_index]
    job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_jobs = []
    for i in job_list:
        job_details = {
            "company": data.iloc[i[0]]['company'],
            "employment_type": data.iloc[i[0]]['employmenttype_jobstatus'],
            "job_location": data.iloc[i[0]]['joblocation_address'],
            "job_title": data.iloc[i[0]]['jobtitle'],
            "skills": data.iloc[i[0]]['skills']
        }
        recommend_jobs.append(job_details)

    return recommend_jobs

# FastAPI route for job recommendations (POST request with JSON body)
@app.post("/recommendations/", response_model=List[JobRecommendationResponse])
async def get_recommendations(request: JobRequest, db: Session = Depends(get_session)):
    print(f"Job Title: {request.job_title}")
    
    # Get job recommendations based on the job title
    recommendations = recommend(request.job_title)
    
    # Convert recommendations to JSON string (no need for .dict() since it's already a dict)
    recommended_jobs_str = json.dumps(recommendations)

    # Insert the new recommendation into the database using SQLAlchemy ORM
    try:
        job_recommendation = JobRecommendationTable(
            job_title=request.job_title,
            recommended_jobs=recommended_jobs_str
        )
        db.add(job_recommendation) 
        db.commit()  
    except Exception as e:
        db.rollback()  
        print(f"Error inserting data: {e}")  
        raise HTTPException(status_code=500, detail="Failed to save recommendations to the database.")
    
    return recommendations


# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)