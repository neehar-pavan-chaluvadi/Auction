import axios from "axios";

const API_URI = "http://localhost:8080/";

const login = (email, password) => {
    return axios
      .post(API_URI + "login", {
        email,
        password,
      })
      .then((response) => {
        if (response.data.username) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }
  
        return response.data;
      });
  };

  const register = (username, profile_name, email, password) =>{
    return axios.post(API_URI + 'users', {
      username,
      profile_name,
      email,
      password
    })
    .then
  }

  const AuthServices = {
    login,
    register,
  }
  export default AuthServices