from flask import Blueprint, request, jsonify
from .model_loader import loader, predict

bp = Blueprint('main', __name__)
model, tokenizer, label_encoder = loader()


@bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data['text']
        prediction = predict(text, model, tokenizer, label_encoder)
        return jsonify({'success': True, 'prediction': prediction})
    except Exception as e:
        return jsonify({'success': False, 'prediction': None})
