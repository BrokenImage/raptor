import React from 'react';
import { connect } from 'react-redux';

class PredictionLabel extends React.Component {
  render() {
    return (
      <div className="container">
        <div className="row">
          {this.props.prediction && (
            <div className="col-md-6">
              <div className="card">
                {this.props.prediction ? this.props.prediction : ''}
              </div>
            </div>
          )}
        </div>
      </div>
    );
  }
}

const mapStateToProps = ({ predict }) => {
  return {
    prediction: predict.prediction,
  };
};

export default connect(mapStateToProps, null)(PredictionLabel);
