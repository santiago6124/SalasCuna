import {React, useContext} from 'react';
import './Menu.css';
import logo from '../../media/logo.png';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

import AuthContext from "../../context/AuthContext";

const Menu = ({link1Text, link1Path, link2Text, link2Path}) => {

  let {user, logoutUser} = useContext(AuthContext)

  return (
    <Navbar expand="lg" className="navbar">
      <Container fluid>
        <Navbar.Brand href="/">
          <img src={logo} alt="logo de" className="logo" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav className="me-auto my-2 my-lg-0" style={{ maxHeight: '100px' }} navbarScroll>
            <Link to={link1Path}>
              <Nav className="titulo">{link1Text}</Nav>
            </Link>
            <Link to={link2Path}>
              <Nav className="titulo">{link2Text}</Nav>
            </Link>
          </Nav>
          <Nav>
            {user ? (
              <Button className="boton" variant="primary" onClick={logoutUser}>
                Log Out
              </Button>
            ) : (
              <Link to="/login">
                <Button className="boton" variant="primary">
                  Log In
                </Button>
              </Link>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Menu;
