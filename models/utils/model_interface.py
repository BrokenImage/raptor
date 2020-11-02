import joblib


class Model:

    def __init__(self):
        # The actual learner used to generate predictions.
        self.model = None

    def fit(self, X_train, y_train):
        '''
        Fit a model on a training dataset.

        Args:
        ---
        X_train: Batch of samples for training. Numpy array of shape (m, n),
        where m is the number of samples and n is the dimension of the
        feature vector.
        y_train: Observed training targets. Numpy array of shape (n,).
        '''
        raise NotImplementedError

    def predict(self, input_features):
        '''
        Function that accepts a model and input data and returns a prediction.

        Args:
        ---
        input_features: Features required by the model to generate prediction.
        Numpy array of shape (1, n) where n is the dimension of the feature
        vector.

        Returns:
        --------
        prediction: Prediction of the model. Numpy array of shape (1,).
        '''
        raise NotImplementedError

    def predict_batch(self, batch_input_features):
        '''
        Function that predicts a batch of sampels.

        Args:
        ---
        batch_input_features: A batch of features required by the model to
        generate predictions. Numpy array of shape (m, n) where m is the 
        number of samples and n is the dimension of the feature vector.

        Returns:
        --------
        prediction: Predictions of the model. Numpy array of shape (m,).
        '''
        raise NotImplementedError

    def preprocess(input_data):
        '''
        Preprocess raw input data.

        Args:
        ---
        input_data - Batch of samples. Numpy array of shape (m, n) where m is
        the number of samples and n is the dimension of the feature vector.
        '''
        raise NotImplementedError

    def persist(self, filename):
        '''
        Serialize the fitted model and metadata to disk. We provide a default
        implementation using the joblib library. This default implementation
        can be overridden by subclasses if 3rd party model objects provide more
        efficient persistence methods. For example, the xgboost library provides
        a method to save xgboost.Booster objects.
        definitions.
        '''
        joblib.dump(self.model, filename)

    def load(self, filename):
        '''
        Load a fitted model from the local filesystem into memory.

        Args:
        ---
        filename: Path to model file.
        '''
        self.model = joblib.load(filename)

    def to_remote(self, persist=True):
        '''
        Store persisted model on a remote filesystem like AWS S3 or Google Cloud
        Storage.

        Args:
        ---
        persist: Whether to persist model to local filesystem before storing
        remotely. Defaults to True.

        Returns:
        --------
        Remote path.
        '''
        raise NotImplementedError

    def from_remote(self, remote_path):
        '''
        Load a fitted model from a remote filesystem into memory.

        Args:
        ---
        remote_path: Remote path to persisted model file.
        '''
        raise NotImplementedError