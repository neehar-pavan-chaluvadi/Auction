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
          sessionStorage.setItem("user", JSON.stringify(response.data));
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
    .then((response) =>{
      console.log(response.data)
      return response.data;
    })
  }

  const fetchProducts = (type) => {
    return axios.get(API_URI + `items?type=${type}`,{
      headers:{
        Authorization: 'Bearer ' + JSON.parse(sessionStorage.getItem("user"))['access_token']
      }
    })
    .then((response) => response.data)
  }

  const AuthServices = {
    login,
    register,
    fetchProducts
  }
  export default AuthServices