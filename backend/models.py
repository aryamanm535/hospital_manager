from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)


class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialization = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)

    appointments = relationship("Appointment", back_populates="doctor")

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)
    address = Column(String)

    appointments = relationship("Appointment", back_populates="patient")

class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"))
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

    __table_args__ = (UniqueConstraint('doctor_id', 'start_time', 'end_time', name='_doctor_appointment_uc'),)