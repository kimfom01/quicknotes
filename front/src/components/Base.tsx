import { ReactElement, ReactNode } from "react";
import "./Base.css";
import logo from "../assets/logo-text.png";
import { Container, Nav, Navbar, Image } from "react-bootstrap";

interface Prop {
  children: ReactNode | ReactElement;
}

export const Base = ({ children }: Prop) => {
  return (
    <main className="base">
      <Container fluid className="mt-3">
        <Navbar collapseOnSelect expand="lg" variant="dark">
          <Navbar.Brand href="/" className="text-light fw-bold">
            <Image className="left-padding" src={logo} alt="Logo text image" />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="ms-auto fs-4 right-padding">
              <span>
                <Nav.Link className="text-orange" href="/">
                  Home
                </Nav.Link>
                <hr />
              </span>
              <Nav.Link className="text-light" href="/about-us">
                About Us
              </Nav.Link>
              <Nav.Link className="text-light" href="/how-it-works">
                How it works
              </Nav.Link>
              <Nav.Link className="text-light" href="/signin">
                Sign In
              </Nav.Link>
              <Nav.Link className="text-light" href="/signup">
                Sign Up
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
        <div>{children}</div>
      </Container>
    </main>
  );
};
