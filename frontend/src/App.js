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
          Here is a big jumbotron, with a container underneath
          <Container>
            Now I am in the container!
            <div className={styles.App}>
              <header className={styles.App_header}>
                <ExampleWrapper url="localhost:8888" />
                <h2 className={styles.header}>Header Content With Futura</h2>
                <h5 className={styles.section}>Section Header</h5>
                <p className={styles.work}>
                  This is content written with the work sans font. The brown fox
                  jumped over the large lake
                </p>
                <p className={styles.section}>
                  MENU written with the Futura. The brown fox jumped over the
                  large lake
                </p>
                <p className={styles.libre}>
                  CAPS This is content written with the libre franklin font. The
                  brown fox jumped over the large lake <GoFlame />
                </p>
                <p>
                  Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                  className={styles.link}
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn React
                </a>
              </header>
            </div>
          </Container>
        </Jumbotron>
      </div>
    );
  }
}

export default App;
