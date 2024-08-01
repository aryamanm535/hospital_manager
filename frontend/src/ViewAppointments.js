import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DataTable from './DataTable';
import './View.css';

const ViewAppointments = ({ token }) => {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    const fetchAppointments = async () => {
      const response = await axios.get('http://127.0.0.1:8000/appointments', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setAppointments(response.data);
    };
    fetchAppointments();
  }, [token]);

  const handleDelete = async (appointment) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/appointments/${appointment.appointment_id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setAppointments(appointments.filter((a) => a.appointment_id !== appointment.appointment_id));
    } catch (error) {
      console.error('Error deleting appointment', error);
    }
  };

  const columns = ['appointment_id', 'doctor_id', 'patient_id', 'start_time', 'end_time'];

  return (
    <div className="container">
      <h2>Appointments</h2>
      <DataTable columns={columns} data={appointments} onDelete={handleDelete} />
    </div>
  );
};

export default ViewAppointments;