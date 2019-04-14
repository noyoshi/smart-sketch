import React, { Component } from "react";

class CanvasTool extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <>
        <div className="colorButtons">
          <h4>Pen Color</h4>
          <input
            type="color"
            list="presetColors"
            id="colorpicker"
            value="#759edf"
            className="colorpicker"
          />
          <datalist id="presetColors">
            <option>#384f83</option>/>
            <option>#efefef</option>
            <option>#2c1e16</option>
            <option>#5d6e32</option>
            <option>#b7d24e</option>
            <option>#3c3b4b</option>
            <option>#987e6a</option>
            <option>#759edf</option>
            <option>#352613</option>
            <option>#636363</option>
            <option>#e670b6</option>
            <option>#c1c3c9</option>
            <option>#776c2d</option>
            <option>#bf602c</option>
            <option>#32604d</option>
          </datalist>
        </div>
        <div className="colorButtons">
          <h4>Backgound Color</h4>
          <input
            type="color"
            list="presetColors"
            value="#ffffff"
            id="bgcolorpicker"
            className="colorpicker"
          />
          <datalist id="presetColors">
            <option>#384f83</option>/>
            <option>#efefef</option>
            <option>#2c1e16</option>
            <option>#5d6e32</option>
            <option>#b7d24e</option>
            <option>#3c3b4b</option>
            <option>#987e6a</option>
            <option>#759edf</option>
            <option>#352613</option>
            <option>#636363</option>
            <option>#e670b6</option>
            <option>#c1c3c9</option>
            <option>#776c2d</option>
            <option>#bf602c</option>
            <option>#32604d</option>
          </datalist>
        </div>

        <div className="toolsButtons">
          <h4>Tools</h4>
          <button id="eraser" className="btn btn-default">
            <span className="glyphicon glyphicon-erase" aria-hidden="true" />
          </button>
          <button id="clear" className="btn btn-danger">
            {" "}
            <span className="glyphicon glyphicon-repeat" aria-hidden="true" />
          </button>
        </div>

        <div className="buttonSize">
          <h4>
            Brush Size *<span id="showSize">5</span>*
          </h4>
          <input
            type="range"
            min="1"
            max="50"
            value="5"
            step="1"
            id="controlSize"
          />
        </div>

        <div className="canvasSize">
          <h4>Canvas</h4>
          <div className="input-group">
            <span className="input-group-addon">X</span>
            <input
              type="number"
              id="sizeX"
              className="form-control"
              placeholder="sizeX"
              value="800"
              className="size"
            />
          </div>
          <div className="input-group">
            <span className="input-group-addon">Y</span>
            <input
              type="number"
              id="sizeY"
              className="form-control"
              placeholder="sizeY"
              value="500"
              className="size"
            />
          </div>
          <input
            type="button"
            className="updateSize btn btn-success"
            value="Update"
            id="canvasUpdate"
          />
        </div>
        <div className="extra">
          <h4>Upload</h4>
          <a
            id="uploadimage"
            className="btn btn-warning"
            onClick={this.props.handleUpload}
          >
            Convert to photo
          </a>
        </div>
      </>
    );
  }
}

export default CanvasTool;
