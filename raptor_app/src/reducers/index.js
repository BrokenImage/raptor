import { combineReducers } from 'redux';
import predicReducer from './predictReducer';

export default combineReducers({
  predict: predicReducer,
});
