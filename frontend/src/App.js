import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './Login';
import Menu from './Menu';
import ViewAppointments from './ViewAppointments';
import AddAppointment from './AddAppointment';
import ViewPatients from './ViewPatients';
import AddPatient from './AddPatient';
import ViewDoctors from './ViewDoctors';
import AddDoctor from './AddDoctor';
import AddUser from './AddUser';

import './App.css';

const App = () => {
  const [token, setToken] = useState('');
  const [username, setUsername] = useState('');
  const [role, setRole] = useState('');

  const handleLogin = (newToken, newUsername, newRole) => {
    setToken(newToken);
    setUsername(newUsername);
    setRole(newRole);
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={!token ? <Login setToken={handleLogin} /> : <Navigate to="/menu" />} />
        <Route path="/menu" element={token ? <Menu username={username} role={role} /> : <Navigate to="/" />} />
        <Route path="/appointments" element={token ? <ViewAppointments token={token} /> : <Navigate to="/" />} />
        <Route path="/add-appointment" element={token ? <AddAppointment token={token} /> : <Navigate to="/" />} />
        <Route path="/patients" element={token ? <ViewPatients token={token} /> : <Navigate to="/" />} />
        <Route path="/add-patient" element={token ? <AddPatient token={token} /> : <Navigate to="/" />} />
        <Route path="/doctors" element={token ? <ViewDoctors token={token} /> : <Navigate to="/" />} />
        <Route path="/add-doctor" element={token ? <AddDoctor token={token} /> : <Navigate to="/" />} />
        <Route path="/add-user" element={token ? <AddUser token={token} /> : <Navigate to="/" />} />
      </Routes>
    </Router>
  );
};

export default App;