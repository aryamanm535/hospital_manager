import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = ({ setToken }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log('Sending login request with:', { username, password });
      const response = await axios.post('http://127.0.0.1:8000/token', new URLSearchParams({ username, password,}), 
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
      
      setToken(response.data.access_token);
      navigate('/menu');
    } catch (error) {
      console.error('Error logging in:', error.response ? error.response.data : error.message);
      setError('Invalid username or password');
    }
  };

  return (
    <div className="container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
        {error && <p className="message">{error}</p>}
      </form>
    </div>
  );
};

export default Login;