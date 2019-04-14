import React, { Component } from "react";
import styles from "../styles/css/App.module.css";
import ExampleButton from "./ExampleButton";
import CanvasTool from "./CanvasTool";
import Img from "react-image";

class GeneratedImage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <>
        <img src={this.props.src} />
      </>
    );
  }
}

export default GeneratedImage;
