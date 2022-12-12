import React, { useState, useEffect, useCallback } from "react";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import AuthServices from "../servicerequests/service";

const AuctionItem = ({id, img,name, description, onBid, base_price, highest_bid, buyer}) =>{
    const [bidAmount, setBidAmount] = useState('')
    return (
        <div className="auction-item-wrapper">
            <img src={img} alt={name} className="auction-image" />
            <div>
                <p className="auction-name">
                    <span>{name}</span><span>currentBid: {highest_bid || base_price}</span></p>
                {buyer &&<p>Buyer: {buyer}</p>}
                <p className="auction-description">{description}</p>
            </div>
            {!buyer && <div className="auction-input-wrapper">
                <input type="number" className="auction-input" placeholder="place your bid" min={base_price} onChange={(e) => setBidAmount(e.target.value)}/>
                <button className="auction-button" onClick={(e) => {
                    if(bidAmount > (highest_bid||base_price)){
                        onBid(id, bidAmount)
                    } else {
                        toast.error('bid amount is less than current highest bid or base price amount', {autoClose: 1000})
                    }
                }}>Increase Bid </button> 
            </div>}
        </div>
    )
}

export const Auction = () => {

    const [products, setProducts] = useState([]);
    const [productType, setProductType] = useState('live');

    const fetchProducts = useCallback((type) =>{
        AuthServices.fetchProducts(type)
        .then((data) =>{
            setProducts(data.items);
        });
    },[])

    useEffect(() =>{
        fetchProducts(productType);
    },[productType, fetchProducts])

    const handleSubmitBid = (id, bidAmount) => {
        AuthServices.updateBid(id, bidAmount)
        .then(() => {
            fetchProducts('live');
        })
    }

    return (
    <div className="auction-page">
        <ToastContainer />
        <div className="auction-filter">
            <button type="button" className={productType === "past" ? "active" : ""} onClick={() => setProductType('past')}>Completed Auctions</button>
            <button type="button" className={productType === "live" ? "active" : ""} onClick={() => setProductType('live')}>Live Auctions</button>
            <button type="button" className={productType === "future" ? "active" : ""} onClick={() => setProductType('future')}>Upcoming Auctions</button>
        </div>
        <div className="auction-wrapper">
            {
                products?.map((product) => <AuctionItem {...product} key={product.id}  onBid={handleSubmitBid}/>)
            }
        </div>
    </div>
    
    )
}