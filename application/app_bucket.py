from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/app/<variable>', methods=['GET'])
def show_variable(variable):
    return jsonify({"message": f"Le mot que vous avez passé est : {variable}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
