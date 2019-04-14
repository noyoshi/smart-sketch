import React, { Component } from "react";
import styles from "../styles/css/App.module.css";
import ExampleButton from "./ExampleButton";
import CanvasTool from "./CanvasTool";
import Img from "react-image";

class UploadWrapper extends Component {
  constructor(props) {
    super(props);

    this.imageUrl = "http://localhost:8888/img/placeholder.png";
    this.handleUpload = this.handleUpload.bind(this);
    this.imageHash = Date.now();
  }

  handleUpload() {
    var dataURL = document.getElementById("canvas").toDataURL("image/png");
    fetch("http://127.0.0.1:8888/upload", {
      method: "POST",
      body: dataURL
    })
      .then(result => result.json())
      .then(r => {
        this.setState(state => ({
          imageUrl: r.location,
          imageHash: Date.now()
        }));
        console.log(this.state);
      });
  }

  render() {
    return (
      <>
        <img src={`${this.imageUrl}?${this.imageHash}`} />
        <CanvasTool handleUpload={this.handleUpload} />
      </>
    );
  }
}

export default UploadWrapper;
