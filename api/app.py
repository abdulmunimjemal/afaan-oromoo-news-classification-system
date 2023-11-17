from flask import Flask, request, jsonify
from model_loader import loader, predict

app = Flask(__name__)
model, tokenizer, label_encoder = loader()


@app.route('/predict', methods=['POST'])
def predict_host():
    try:
        data = request.get_json()
        if 'text' not in data:
            raise ValueError("Missing 'text' in the request body")
        text = data['text']
        prediction = predict(text, model, tokenizer, label_encoder)
        return jsonify({'success': True, 'prediction': prediction})
    except ValueError as ve:
        # bad request
        return jsonify({'success': False, 'error': str(ve)}), 400
    except Exception as e:
        # Internal server error
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)
