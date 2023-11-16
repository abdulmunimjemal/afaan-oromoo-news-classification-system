from flask import Flask, request, jsonify
from model_loader import loader, predict

model, tokenizer, label_encoder = loader()

app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])
def predict_host():
    text = request.args.get('text')
    # text = data['text']
    prediction = str(predict(text, model, tokenizer, label_encoder))
    print("PREDICRION: ", prediction)
    return jsonify({'success': True, 'prediction': prediction})
    return jsonify({'success': False, 'prediction': None})


if __name__ == '__main__':
    app.run(debug=True)
