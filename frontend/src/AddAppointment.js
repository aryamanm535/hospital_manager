import React, { useState } from 'react';
import axios from 'axios';

//creating appointment constant variables along with use states
const AddAppointment = ({ token }) => {
  const [doctorId, setDoctorId] = useState('');
  const [patientId, setPatientId] = useState('');
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://127.0.0.1:8000/appointments', {
        doctor_id: doctorId,
        patient_id: patientId,
        start_time: startTime,
        end_time: endTime,
      }, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      setMessage('Appointment added successfully');
    } catch (error) {
      setMessage('Error adding appointment');
    }
  };

  return (
    <div>
      <h2>Add Appointment</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Doctor ID:</label>
          <input
            type="text"
            value={doctorId}
            onChange={(e) => setDoctorId(e.target.value)}
          />
        </div>
        <div>
          <label>Patient ID:</label>
          <input
            type="text"
            value={patientId}
            onChange={(e) => setPatientId(e.target.value)}
          />
        </div>
        <div>
          <label>Start Time:</label>
          <input
            type="datetime-local"
            value={startTime}
            onChange={(e) => setStartTime(e.target.value)}
          />
        </div>
        <div>
          <label>End Time:</label>
          <input
            type="datetime-local"
            value={endTime}
            onChange={(e) => setEndTime(e.target.value)}
          />
        </div>
        <button type="submit">Add Appointment</button>
        {message && <p>{message}</p>}
      </form>
    </div>
  );
};

export default AddAppointment;