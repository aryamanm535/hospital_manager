from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        arbitrary_types_allowed = True

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone_number: str
    email: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    doctor_id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    name: str
    date_of_birth: datetime
    phone_number: str
    email: str
    address: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int

    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int
    start_time: datetime
    end_time: datetime

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    appointment_id: int

    class Config:
        orm_mode = True