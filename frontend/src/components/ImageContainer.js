import React, { Component } from "react";
import styles from "../styles/css/App.module.css";
import Img from "react-image";
import Upload from "./Uploader/Upload";

/* Example Hero that we can customize */
class ImageContainer extends Component {
  constructor(props) {
    super(props);
    this.state = { imageAvaliable: false };
    this.imageUrl = "http://localhost:8888/img/example.jpg";
  }

  handleUpload(file) {
    fetch("http://127.0.0.1:8888/upload", {
      method: "POST",
      body: file // This is your file object,
    })
      .then(response => response.json())
      .then(
        success => {
          this.setState(state => ({
            imageUrl: success.location
          }));
        } // Handle the success response object
      )
      .catch(
        error => console.log(error) // Handle the error response object
      )
      .bind(this);
  }

  render() {
    return (
      <>
        <Upload handleUpload={this.handleUpload} />
        <Img src={this.imageUrl} />
      </>
    );
  }
}

export default ImageContainer;
