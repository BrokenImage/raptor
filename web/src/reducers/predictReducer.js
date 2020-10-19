const INITIAL_STATE = {
  prediction: '',
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case 'UPDATE_PREDICTION':
      return {
        ...state,
        prediction: action.payload,
      };
    default:
      return state;
  }
};
