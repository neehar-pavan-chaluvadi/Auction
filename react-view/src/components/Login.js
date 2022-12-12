import React, { useState } from "react";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import AuthServices from "../servicerequests/service";

export const Login = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        AuthServices.login(email, pass).then((response) => {
            props.compSwitch('auction')
        }).catch((error) => {
            toast.error('Invalid Username or Password');
            console.error(error);
        })
    }

    return (
        <div className="auth-form-container">
            <ToastContainer />
            <h2>Login</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="email">email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="email" id="email" name="email" />
                <label htmlFor="password">password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="password" id="password" name="password" />
                <button type="submit">Log In</button>
            </form>
            <button className="link-btn" onClick={() => props.compSwitch('register')}>Don't have an account? Register here.</button>
        </div>
    )
}