import React from 'react';
import Header from './Header/Header';
import BurgerBuilder from './BurgerBuilder/BurgerBuilder';
import Checkout from './Orders/Checkout/Checkout';
import Orders from './Orders/Orders';
import { Route } from 'react-router-dom';


const Main = props => {
    return (
        <div>
            <Header />
            <div className="container">
                <Route path="/Orders" component={Orders} />
                <Route path="/Checkout" component={Checkout} />
                <Route path="/" exact component={BurgerBuilder} />
            </div>


        </div>
    )
}


export default Main; 