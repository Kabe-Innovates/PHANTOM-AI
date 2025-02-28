from flask import Flask, request, jsonify
from deception_responder import deploy_deception

app = Flask(__name__)

@app.route("/cognitive_deception", methods=["POST"])
def cognitive_deception():
    data = request.json
    ip = data["ip"]
    method = data["method"]
    severity = data["severity"]
    frequency = data["frequency"]
    tools_used = data["tools_used"]

    attacker_type = classify_attacker(severity, frequency, tools_used)
    deception = deploy_deception(attacker_type)

    return jsonify({
        "attacker_ip": ip,
        "attack_method": method,
        "attacker_type": attacker_type,
        "deception_applied": deception
    })

def classify_attacker(severity, frequency, tools_used):
    """Mock function to classify attacker based on input."""
    if severity > 7:
        return "Advanced Persistent Threat"
    elif frequency > 10:
        return "Hacktivist"
    else:
        return "Script Kiddie"

if __name__ == "__main__":
    app.run(debug=True)
