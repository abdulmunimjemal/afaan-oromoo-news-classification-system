from flask import Flask, request, jsonify, render_template
from model_loader import loader, predict
from collections import defaultdict

app = Flask(__name__)
model, tokenizer, label_encoder = loader()

categories = defaultdict(str)
categories = {
    'biiznasii': 'Business (Biiznasii)',
    'fayyaa': 'Health (Fayyaa)',
    'idil_addunyaa': 'World Wide (Idil Addunyaa)',
    'ispoortii': 'Sport  (Ispoortii)',
    'teeknooloojii': 'Technology (Teeknooloojii)',
    'oduu_biyya_keessaa': 'Local News (Oduu Biyya Keessaa)'
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.form
            if 'text' not in data:
                raise ValueError("Missing 'text' in the request body")
            text = data['text']
            if len(text.split()) < 30:
                raise ValueError(
                    "Text must be at least 30 words long. Please enter a longer text.")
            prediction = predict(text, model, tokenizer, label_encoder)
            return render_template('predict.html', prediction=categories[prediction])
        except ValueError as ve:
            # bad request.
            return render_template('predict.html', error=str(ve)), 400
        except Exception as e:
            # Server Error
            return render_template('predict.html', error=str(e)), 500
    else:
        return render_template('predict.html')

# api version


@app.route('/api/predict', methods=['POST'])
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
