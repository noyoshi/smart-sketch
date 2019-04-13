import React, { Component } from "react";
import styles from "../styles/css/App.module.css";

/* Example Hero that we can customize */
class Hero extends Component {
  render() {
    return (
      <div className={styles.heroContainer}>
        <p className={styles.heroText}>This is where the hero goes</p>
      </div>
    );
  }
}

export default Hero;
