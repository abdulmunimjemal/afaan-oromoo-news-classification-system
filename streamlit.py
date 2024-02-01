import streamlit as st
from api.model_loader import loader, predict
from collections import defaultdict

model, tokenizer, label_encoder = loader(model_path="models/trained_models/model_20231116_accuracy_0.9263.h5", tokenizer_path="models/trained_models/tokenizer.joblib", label_encoder_path="models/trained_models/label_encoder.joblib")

categories = defaultdict(str)
categories = {
    'biiznasii': 'Business (Biiznasii)',
    'fayyaa': 'Health (Fayyaa)',
    'idil_addunyaa': 'World Wide (Idil Addunyaa)',
    'ispoortii': 'Sport  (Ispoortii)',
    'teeknooloojii': 'Technology (Teeknooloojii)',
    'oduu_biyya_keessaa': 'Local News (Oduu Biyya Keessaa)'
}

def predict_text(text):
    try:
        if len(text.split()) < 20:
            raise ValueError("Text must be at least 20 words long. Please enter a longer text.")
        
        prediction = predict(text, model, tokenizer, label_encoder, confidence=True)
        return (categories[prediction[0]], prediction[1])
    except ValueError as ve:
        return (str(ve), 1)
    except Exception as e:
        return (str(e), 1)

def main():
    st.title('Afaan Oromoo News Category Prediction')

    text_input = st.text_area('Enter your news text:', '')

    if st.button('Predict'):
        prediction = predict_text(text_input)
        st.write(f'Predicted Category: {prediction[0]}')
        st.write(f'Confidence: {round(prediction[1]*100, 2)}%')

if __name__ == '__main__':
    main()