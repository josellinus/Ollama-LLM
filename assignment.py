import ollama
from flask import Flask, request, jsonify

model_name = 'moondream'
app = Flask(__name__)

def generate_response(prompt):
    response = ollama.generate(model=model_name, prompt=prompt)
    return response

@app.route('/inference', methods=['POST'])
def inference():
    data = request.get_json()

    if 'prompt' not in data:
        return jsonify({'error': 'no input'}), 400
    prompt = data['prompt']

    try:
        response = generate_response(prompt)
        return jsonify({'model': response['model'], 'response': response['response']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)