import random
import time
import json

# Simulate an attack with varying severity, frequency, and tools used
attacks = [
    {"severity": 3, "frequency": 2, "tools_used": 1, "attack_method": "Phishing"},
    {"severity": 8, "frequency": 5, "tools_used": 4, "attack_method": "SQL Injection"},
    {"severity": 5, "frequency": 12, "tools_used": 2, "attack_method": "DDoS"},
]

# Example function to classify the attacker
def classify_attacker(severity, frequency, tools_used):
    if severity > 7:
        return "Advanced Persistent Threat"
    elif frequency > 10:
        return "Hacktivist"
    else:
        return "Script Kiddie"

# Example function to apply deception strategy
def deploy_deception(attacker_type):
    deception_responses = {
        "Script Kiddie": ["Fake login error", "Redirect to sandbox", "Inject fake credentials"],
        "Advanced Persistent Threat": ["Deploy Cowrie SSH Honeypot", "Send fake admin credentials", "Trigger alert"],
        "Hacktivist": ["Simulate fake DDoS countermeasures", "Fake traffic shaping alerts", "Log and track botnet behavior"],
    }
    return random.choice(deception_responses.get(attacker_type, ["No deception available"]))

# Simulate a running attack
def run_demo():
    for attack in attacks:
        attacker_type = classify_attacker(attack['severity'], attack['frequency'], attack['tools_used'])
        deception = deploy_deception(attacker_type)
        log_entry = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "attacker_ip": f"192.168.1.{random.randint(100, 150)}",  # Dynamic attacker IP
            "attack_method": attack['attack_method'],
            "severity": attack['severity'],
            "frequency": attack['frequency'],
            "tools_used": attack['tools_used'],
            "attacker_type": attacker_type,
            "deception_applied": deception
        }
        print(json.dumps(log_entry, indent=4))
        
        # Log to file
        with open("deception_logs.json", "a") as log_file:
            json.dump(log_entry, log_file)
            log_file.write("\n")
        
        time.sleep(1)  # Simulate time delay between attacks

# Run the demo
run_demo()
