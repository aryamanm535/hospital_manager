from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from models import Base
from schemas import UserCreate, User, DoctorCreate, Doctor, PatientCreate, Patient, AppointmentCreate, Appointment, UserLogin, Token
import crud
from crud import create_user, create_patient, create_appointment, create_doctor, get_user_by_username, delete_doctor, delete_patient, delete_appointment, get_appointments_by_patient, verify_user
from database import engine
from dependencies import get_db
import auth
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",  # React app URL
    "http://127.0.0.1:3000"   # React app URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token", response_model=Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.verify_user(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", 
    "username": user.username,
    "role": user.role}

@app.post("/doctors/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return crud.create_doctor(db=db, doctor=doctor)

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    try:
        crud.delete_doctor(db=db, doctor_id=doctor_id)
        return {"message": "Doctor deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/patients/", response_model=Patient)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return crud.create_patient(db=db, patient=patient)

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    try:
        crud.delete_patient(db=db, patient_id=patient_id)
        return {"message": "Patient deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db=db, appointment=appointment)

@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    try:
        crud.delete_appointment(db=db, appointment_id=appointment_id)
        return {"message": "Appointment deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/patients/{patient_id}/appointments/", response_model=List[Appointment])
def get_appointments_by_patient(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return crud.get_appointments_by_patient(db, patient_id)

@app.get("/doctors/", response_model=List[Doctor])
def get_doctors(db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return crud.get_doctors(db=db)

@app.get("/patients/", response_model=List[Patient])
def get_patients(db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return crud.get_patients(db=db)

@app.get("/appointments/", response_model=List[Appointment])
def get_appointments(db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return crud.get_appointments(db=db)
