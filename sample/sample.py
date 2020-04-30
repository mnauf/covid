def preprocess(data):
    """
    Prepare the data for input to our model

    Inputs:
    - data: A pandas dataframe of shape (m, ?) containing the input data

    Outputs:
    - A numpy array of shape (m, ?) containing the processed data
    """
    
    # load the cough, breathing, or finger files from disk
    
    # trim / remove noise / etc.

def predict(data, h5):
    """
    Sample file for the API of individual models

    Inputs:
    - data: A pandas dataframe of shape (m, ?) containing the input data
    - h5: The best trained model file for this class

    Outputs:
    - A numpy array of shape (m, 1) outputting the predicted probability of
      COVID-19 by this model
    """

    # data_proc = preprocess(data)
    #model = load_model(h5)
    #pred = model.predict(data_proc)

    print("h5 file: ", h5)

    return pred
