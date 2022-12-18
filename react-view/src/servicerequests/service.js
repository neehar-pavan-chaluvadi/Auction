import axios from "axios";

const API_URI = "http://localhost:8089/";

export const getStorageDetails = () => JSON.parse(sessionStorage.getItem('user'))

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

const logout = () => {
  const access_token = getStorageDetails()['access_token'];
  return axios.delete(API_URI + "logout", {
    headers:{
      Authorization: 'Bearer ' + access_token
    }
  })
    .then((response) => response.data)
}

  const register = (username, profile_name, email, password) =>{
    return axios.post(API_URI + 'register', {
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
    const access_token = getStorageDetails()['access_token'];
    return axios.get(API_URI + `items?type=${type}`,{
      headers:{
        Authorization: 'Bearer ' + access_token
      }
    })
    .then((response) => response.data)
  }

  const updateBid = (id, bidAmount) =>{
    const userDetails = getStorageDetails();
    const access_token = userDetails['access_token'];
    const username = userDetails['username'];

    return axios.put(API_URI + 'raise_bid',{
      product_id: id,
      username,
      amount: bidAmount
    },{headers:{
      Authorization: 'Bearer '  + access_token
    }})
    .then(response =>{
      console.log(response.data);
      return response.data;
    })
  }

  const AuthServices = {
    login,
    register,
    fetchProducts,
    updateBid,
    logout
  }
  export default AuthServices
