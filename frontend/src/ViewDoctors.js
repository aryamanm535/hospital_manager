import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DataTable from './DataTable';
import './View.css';

const ViewDoctors = ({ token }) => {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    const fetchDoctors = async () => {
      const response = await axios.get('http://127.0.0.1:8000/doctors', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setDoctors(response.data);
    };
    fetchDoctors();
  }, [token]);

  const handleDelete = async (doctor) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/doctors/${doctor.doctor_id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setDoctors(doctors.filter((d) => d.doctor_id !== doctor.doctor_id));
    } catch (error) {
      console.error('Error deleting doctor', error);
    }
  };

  const columns = ['doctor_id', 'name', 'specialization', 'phone_number', 'email'];

  return (
    <div className="container">
      <h2>Doctors</h2>
      <DataTable columns={columns} data={doctors} onDelete={handleDelete} />
    </div>
  );
};

export default ViewDoctors;