import React, { Component } from "react";
// React won't pickup the css modules without the name ".module.css"
// - this is useful cuz we can use autocomplete now by using this
import styles from "./styles/css/App.module.css";
import MyNavBar from "./components/MyNavBar";
import Hero from "./components/Hero";
import ExampleWrapper from "./components/ExampleWrapper";
import Container from "react-bootstrap/Container";
import Jumbotron from "react-bootstrap/Jumbotron";
import { GoFlame } from "react-icons/go";
import ImageContainer from "./components/ImageContainer";
import UploadWrapper from "./components/UploadWrapper";

class App extends Component {
  render() {
    return (
      <div>
        <MyNavBar />
        <Hero />
        <Jumbotron>
          <Container>
            <UploadWrapper />
          </Container>
        </Jumbotron>
      </div>
    );
  }
}

export default App;
