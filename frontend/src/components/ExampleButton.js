import React, { Component } from "react";
import Button from "react-bootstrap/Button";
import styles from "../styles/css/App.module.css";

/* Example Hero that we can customize */
class ExampleButton extends Component {
  constructor(props) {
    super(props);
  }

  // toggle came from the upper level component - it is still bound to it
  render() {
    return (
      <Button onClick={this.props.toggle} variant="primary">
        Primary
      </Button>
    );
  }
}

export default ExampleButton;
