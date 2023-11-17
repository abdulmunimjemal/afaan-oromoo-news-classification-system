from flask import Flask, request, jsonify, render_template
from model_loader import loader, predict

app = Flask(__name__)
model, tokenizer, label_encoder = loader()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.form
            if 'text' not in data:
                raise ValueError("Missing 'text' in the request body")
            text = data['text']
            prediction = predict(text, model, tokenizer, label_encoder)
            return render_template('predict.html', prediction=prediction)
        except ValueError as ve:
            return render_template('predict.html', error=str(ve)), 400
        except Exception as e:
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
