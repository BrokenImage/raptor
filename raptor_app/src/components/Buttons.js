import React from 'react';
import './Buttons.css';

function Buttons() {
  return (
    <div className="container">
      <div className="row">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <div>
                <h1> Select Type: </h1>
                <button type="button" class="btn btn-primary">
                  Binary
                </button>
                &nbsp;
                <button type="button" class="btn btn-secondary">
                  Multi
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Buttons;
