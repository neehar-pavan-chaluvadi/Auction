import React, { useState, useEffect } from "react";
import AuthServices from "../servicerequests/service";

export const Auction = (props) => {

    const [products, setProducts] = useState([]);

    useEffect(() =>{
        AuthServices.fetchProducts('live')
        .then((data) =>{
            setProducts(data);
        });
    },[])

    return (
    <div>
        Auction Page
    </div>
    )
}