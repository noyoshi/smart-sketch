import React, { Component } from "react";
// import styles from "../styles/css/App.module.css";
import { GoFlame } from "react-icons/go";
import Navbar from "react-bootstrap/Navbar";

/* Example Navbar that we can customize */
class MyNavBar extends Component {
  state = {
    isTop: true
  };

  componentDidMount() {
    document.addEventListener("scroll", () => {
      const isTop = window.scrollY < 80;
      if (isTop !== this.state.isTop) {
        this.setState({ isTop });
      }
    });
  }

  // NOTE transparent is not a builtin - instead I make my own background class
  // called bg-transparent - all bg="" does it set a class name to bg-""
  render() {
    return (
      <>
        <Navbar
          varient="dark"
          bg={this.state.isTop ? "dark" : "transparent"}
          sticky="top"
        >
          <Navbar.Brand href="#home">
            <div className="appName">
              <GoFlame />
              {" App Name"}
            </div>
          </Navbar.Brand>
        </Navbar>
      </>
    );
  }
}

export default MyNavBar;
