import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DataTable from './DataTable';
import './View.css';

const ViewPatients = ({ token }) => {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    const fetchPatients = async () => {
      const response = await axios.get('http://127.0.0.1:8000/patients', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setPatients(response.data);
    };
    fetchPatients();
  }, [token]);

  const handleDelete = async (patient) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/patients/${patient.patient_id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setPatients(patients.filter((p) => p.patient_id !== patient.patient_id));
    } catch (error) {
      console.error('Error deleting patient', error);
    }
  };

  const columns = ['patient_id', 'name', 'date_of_birth', 'phone_number', 'email', 'address'];

  return (
    <div className="container">
      <h2>Patients</h2>
      <DataTable columns={columns} data={patients} onDelete={handleDelete} />
    </div>
  );
};

export default ViewPatients;