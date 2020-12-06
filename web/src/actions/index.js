const updatePrediction = (prediction) => (dispatch) => {
  dispatch({
    type: 'UPDATE_PREDICTION',
    payload: prediction,
  });
};