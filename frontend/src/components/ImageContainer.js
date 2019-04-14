import React, { Component } from "react";
import styles from "../styles/css/App.module.css";
import Img from "react-image";
import Upload from "./Uploader/Upload";

/* Example Hero that we can customize */
class ImageContainer extends Component {
  constructor(props) {
    super(props);
    this.state = { imageAvaliable: false };
  }

  render() {
    return (
      <>
        <Upload />
        <Img
          src={
            this.imageAvaliable
              ? "http://localhost:8888/img/placeholder.jpg"
              : "http://localhost:8888/img/example.jpg"
          }
        />
      </>
    );
  }
}

export default ImageContainer;
