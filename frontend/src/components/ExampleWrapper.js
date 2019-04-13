import React, { Component } from "react";
import styles from "../styles/css/App.module.css";
import ExampleButton from "./ExampleButton";

class ExampleWrapper extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isToggleOn: true };

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
  }

  // This is the function we will pass to a child component that is still bound to
  // us -> it will let that component modify something up here!
  handleClick() {
    fetch(`http://${this.props.url}`, { mode: "cors" })
      .then(response => response.json())
      .then(response => {
        // We have the JSON response here!
        console.log(JSON.stringify(response));

        // We trigger the wrapper function here!!!
        this.setState(state => ({
          isToggleOn: !state.isToggleOn
        }));
      });
  }

  render() {
    return (
      <div>
        <ExampleButton toggle={this.handleClick} />
        <p> {this.state.isToggleOn ? "ON" : "OFF"} </p>
      </div>
    );
  }
}

export default ExampleWrapper;
