import React, { useState } from "react";
import logo from './logo.svg';
import auction from './images/auction.png'
import './App.css';
import { Login } from "./components/Login";
import { Register } from "./components/Register";
import { Auction } from "./components/Auction";

function App() {
  const [currentForm, setCurrentForm] = useState('login');
  const NavBar = () => (
    <header className='navbar'>
      <a className="navinfo">
        <img src={auction} className='img-logo'></img><span className="logo-label">Auction House</span>
        </a>

        {JSON.parse(sessionStorage.getItem('user'))['username'] && <span className="">{JSON.parse(sessionStorage.getItem('user'))['username']}</span>}
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
      {currentForm === "auction" && <Auction compSwitch={toggleForm} />}
    </div>
    </div>
  );
}

export default App;