import React, { Component } from 'react';
import { connect } from 'react-redux';

import { updatePrediction } from '../actions/index';

class MultipleImageUploadComponent extends Component {
  fileObj = [];
  fileArray = [];

  constructor(props) {
    super(props);
    this.state = {
      file: [null],
    };
    this.uploadMultipleFiles = this.uploadMultipleFiles.bind(this);
    this.uploadFiles = this.uploadFiles.bind(this);
  }

  uploadMultipleFiles(e) {
    this.fileObj.push(e.target.files);
    for (let i = 0; i < this.fileObj[0].length; i++) {
      this.fileArray.push(URL.createObjectURL(this.fileObj[0][i]));
    }
    this.setState({ file: this.fileArray });
  }

  uploadFiles(e) {
    e.preventDefault();
    const data = new FormData();
    data.append('file', this.fileArray[0]);

    fetch('api/multi', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((data) => {
        console.log(data);
        this.updatePrediction(data.prediction);
      });
    });
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <div className="card">
              <div className="card-header">Image Upload Preview</div>
              <div className="card-body">
                <form>
                  <div className="form-group multi-preview">
                    {(this.fileArray || []).map((url) => (
                      <img src={url} alt="..." />
                    ))}
                  </div>

                  <div className="form-group">
                    <input
                      type="file"
                      className="form-control"
                      onChange={this.uploadMultipleFiles}
                      multiple
                    />
                  </div>
                  <button
                    type="button"
                    className="btn btn-success btn-block"
                    onClick={this.uploadFiles}
                  >
                    Upload
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default connect(null, { updatePrediction })(
  MultipleImageUploadComponent
);