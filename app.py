from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sanitize', methods=['POST'])
def sanitize():
    data = request.json
    file_name = data.get('fileName', '')
    template_id = data.get('templateId', '')

    # Reemplaza los espacios en file_name con guiones
    sanitized_file_name = file_name.replace(' ', '-')
    result = f'cachename_{sanitized_file_name}{template_id}'

    return jsonify({'sanitizedFileName': result})


@app.route('/sanitize', methods=['GET'])
def sanitizeGet():
    data = "test hello"
    return jsonify({'sanitizedFileName': data})

if __name__ == '__main__':
    app.run(debug=True)