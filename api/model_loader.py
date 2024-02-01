import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
import joblib
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from preprocessing import preprocessing_pipeline

current_dir = os.getcwd()
main_path = '../models/trained_models/'
model = 'model_20231116_accuracy_0.9263.h5'
tokenizer = 'tokenizer.joblib'
label_encoder = 'label_encoder.joblib'

model_path, tokenizer_path, label_encoder_path = os.path.join(current_dir,main_path, model), os.path.join(
    main_path, tokenizer), os.path.join(main_path, label_encoder)


def loader(model_path=model_path, tokenizer_path=tokenizer_path, label_encoder_path=label_encoder_path):
    # Load the model
    loaded_model = load_model(model_path)

    # Load the tokenizer
    with open(tokenizer_path, 'rb') as tokenizer_file:
        loaded_tokenizer = joblib.load(tokenizer_file)

    # Load the label encoder
    loaded_label_encoder = joblib.load(label_encoder_path)

    return loaded_model, loaded_tokenizer, loaded_label_encoder


def predict(text, loaded_model, loaded_tokenizer, loaded_label_encoder, confidence=False):
    # Preprocess the text
    preprocessor = preprocessing_pipeline.PreprocessingPipeline()
    preprocessed_text = preprocessor.preprocess(text)

    # Tokenize and pad the sequence
    sequence = loaded_tokenizer.texts_to_sequences([preprocessed_text])
    max_length = loaded_model.input_shape[1]
    padded_sequence = pad_sequences(
        sequence, maxlen=max_length, padding='post')

    # Make predictions
    predictions = loaded_model.predict(padded_sequence)

    # Decode the predictions using the loaded label encoder
    predicted_category_index = predictions.argmax()
    predicted_category = loaded_label_encoder.inverse_transform(
        [[predicted_category_index]])[0]

    return (predicted_category, predictions[0][predicted_category_index]) if confidence else predicted_category
