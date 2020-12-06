import React, { Component } from "react";

export default class MultipleImageUploadComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      fileUrlArray: [],
      isLoading: false,
      predictions: []
    };
    this.saveSelectedFiles = this.saveSelectedFiles.bind(this);
    this.handleImageUpload = this.handleImageUpload.bind(this);
  }

  saveSelectedFiles(e) {
    const newFileUrls = [];
    for (let i = 0; i < e.target.files.length; i++) {
      newFileUrls.push(URL.createObjectURL(e.target.files[i]));
    }
    const newFiles = [];
    for (let i = 0; i < e.target.files.length; i++) {
      newFiles.push(e.target.files[i]);
    }
    this.setState({ fileUrlArray: newFileUrls });
    this.setState({ files: newFiles });
  }

  handleImageUpload(e) {
    e.preventDefault();

    const data = new FormData();
    this.state.files.forEach((imageFile) => {
      data.append("files", imageFile);
    });

    const proxyurl = "https://cors-anywhere.herokuapp.com/";
    fetch(`${proxyurl + process.env.REACT_APP_API_URL}/api/classify`, {
      method: "POST",
      body: data,
    })
      .then((res) => {
        this.setState({ isLoading: false });
        return res.json();
      })
      .then((data) => {
        console.log(data); // The api prediction response is found here
        this.setState({ predictions: data })
      })
      .catch((error) => {
        this.setState({ isLoading: false });
        console.log("Error", error);
      });
  }

  render() {
    return (
      <form onSubmit={this.handleImageUpload}>
        <div className="form-group multi-preview">
          {(this.state.fileUrlArray || []).map((url, index) => (
            <img key={index} src={url} alt="..." />
          ))}
        </div>

        <div className="form-group">
          <input
            type="file"
            className="form-control"
            onChange={this.saveSelectedFiles}
            multiple
          />
        </div>
        {!this.state.isLoading && (
          <button type="submit" className="btn btn-success btn-block">
            Upload
          </button>
        )}
        {this.state.isLoading && (
          <button disabled={true} className="btn btn-success btn-block">
            Loading...
          </button>
        )}
        <br />
        <h1>Prediction: {this.state.predictions.prediction}</h1>
      </form>
    );
  }
}
