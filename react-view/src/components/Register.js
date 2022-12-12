import React, { useState } from "react";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import AuthServices from "../servicerequests/service";

export const Register = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');
    const [profile, setProfile] = useState('');


    const handleSubmit = (e) => {
        e.preventDefault();
        AuthServices.register(name, profile, email, pass)
        .then((response) => {
            console.log(response);
            toast('User registration successful')
            props.compSwitch('login')
        })
    }

    return (
        <div className="auth-form-container">
            <ToastContainer />
            <h2>Register</h2>
        <form className="register-form" onSubmit={handleSubmit}>
            <label htmlFor="name">Full name</label>
            <input value={name} name="name" onChange={(e) => setName(e.target.value)} id="name" placeholder="full Name" />

            <label htmlFor="name">Profile name</label>
            <input value={profile} name="profile" onChange={(e) => setProfile(e.target.value)} id="profile" placeholder="Profile Name" />
            <label htmlFor="email">email</label>
            <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
            <label htmlFor="password">password</label>
            <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
            <button type="submit">Register</button>
        </form>
        <button className="link-btn" onClick={() => props.compSwitch('login')}>Already have an account? Login here.</button>
    </div>
    )
}