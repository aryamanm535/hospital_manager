import React from 'react';
import { Link } from 'react-router-dom';
import './Menu.css';

const menuItems = [
  {
    category: 'Appointments',
    items: [
      { text: 'View Appointments', link: '/appointments' },
      { text: 'Add Appointment', link: '/add-appointment' },
    ],
  },
  {
    category: 'Doctors',
    items: [
      { text: 'View Doctors', link: '/doctors' },
      { text: 'Add Doctor', link: '/add-doctor' },
    ],
  },
  {
    category: 'Patients',
    items: [
      { text: 'View Patients', link: '/patients' },
      { text: 'Add Patient', link: '/add-patient' },
    ],
  },
  {
    category: 'Users',
    items: [
      { text: 'Add User', link: '/add-user' },
    ],
  },
];

const Menu = ({ username, role }) => {
  return (
    <div className="menu-container">
      <header>
        <h1>Hospital Management System</h1>
        <div className="user-info">
          {username} logged in as {role}
        </div>
      </header>
      <div className="menu-grid">
        {menuItems.map((category) => (
          <div key={category.category} className="menu-category">
            <h2>{category.category}</h2>
            {category.items.map((item) => (
              <div className="menu-card" key={item.text}>
                <Link to={item.link} className="menu-link">
                  <div className="menu-card-content">
                    <h3>{item.text}</h3>
                  </div>
                </Link>
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Menu;