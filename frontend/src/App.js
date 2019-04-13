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

class App extends Component {
  render() {
    console.log(styles.black);
    return (
      <div>
        <MyNavBar />
        <Hero />
        <Jumbotron>
          <Container>
            <div className={styles.App}>
              <header className={styles.App_header}>
                <h2 className={styles.header}>Upload your file here!</h2>
                <ImageContainer />
              </header>
            </div>
          </Container>
        </Jumbotron>
      </div>
    );
  }
}

export default App;
