import React, { useState } from "react";
import auction from './images/auction.png'
import './App.css';
import { Login } from "./components/Login";
import { Register } from "./components/Register";
import { Auction } from "./components/Auction";
import { getStorageDetails } from "./servicerequests/service";

function App() {
  const userDetails = getStorageDetails();
  const [currentForm, setCurrentForm] = useState(userDetails?.username ? 'auction': 'login');
  
  const onLogout = () => {
      sessionStorage.clear();
      setCurrentForm('login');
  }
  const NavBar = () => (
    <header className='navbar'>
      <div className="navinfo">
        <img src={auction} className='img-logo' alt="logo"></img><span className="logo-label">Auction House</span>
      </div>
        {userDetails?.username && <button onClick={onLogout}><span className="nav-username">{userDetails?.username} <i className="bi bi-box-arrow-left"></i></span></button>}
    </header>
  );

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div>
    <NavBar></NavBar>
    <div className="App">
      {
        currentForm === "login" && <Login compSwitch={toggleForm} /> 
      }
      {
        currentForm === "register" && <Register compSwitch={toggleForm} />
      }
      {currentForm === "auction" && <Auction />}
    </div>
    </div>
  );
}

export default App;