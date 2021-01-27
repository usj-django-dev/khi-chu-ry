import React from 'react';
import './Header.css';
import { NavLink } from 'react-router-dom';


import {
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
} from 'reactstrap';

import Logo from '../../assets/logo.png';


const Header = () => {
    return (
        <div className="Navigation">
            <Navbar style={{
                backgroundColor: "#D70F64",
                height: "70px",

            }} >
                <NavbarBrand href="/" className="mr-auto ml-md-5 Brand ">
                    <img src={Logo} alt="Logo" width="80px" />
                </NavbarBrand>
                <Nav className="mr-md-5">
                    <NavItem>
                        <NavLink exact to="/" className="NavLink"> Burger Builder  </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink exact to="/orders" className="NavLink"> Orders  </NavLink>
                    </NavItem>
                </Nav>
            </Navbar>
        </div>
    )

}

export default Header;