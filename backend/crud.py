from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username, models.User.password == password).first()
    return user

def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).first()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).delete()
    db.commit()

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db.query(models.Patient).filter(models.Patient.patient_id == patient_id).delete()
    db.commit()

def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    # Check for overlapping appointments
    overlapping_appointments = db.query(models.Appointment).filter(
        models.Appointment.doctor_id == appointment.doctor_id,
        and_(
            models.Appointment.start_time < appointment.end_time,
            models.Appointment.end_time > appointment.start_time
        )
    ).first()

    if appointment.start_time >= appointment.end_time:
        raise HTTPException(status_code=400, detail="start time must be before end time")

    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).delete()
    db.commit()

def get_appointments_by_patient(db: Session, patient_id: int):
    return db.query(models.Appointment).filter(models.Appointment.patient_id == patient_id).all()