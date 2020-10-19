import React from 'react'
import './Landing.css'
import { NavLink } from 'react-router-dom'

function Landing() {
  return (
    <div className="Header">
      <header>
        <h1>Sonomaly</h1>
        <div>
        <NavLink
            className='nav-link'
            activeClassName='nav-link-active'
            exact to='/'>Home</NavLink>
          <NavLink
            className='nav-link'
            activeClassName='nav-link-active'
            exact to='/login'>Login</NavLink>
        </div>
      </header>
    </div>
  );
}

export default Landing;