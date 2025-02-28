import random

# Deception strategies for each attacker type
deception_responses = {
    "Script Kiddie": ["Fake login error", "Redirect to sandbox", "Inject fake credentials"],
    "Advanced Persistent Threat": ["Deploy Cowrie SSH Honeypot", "Send fake admin credentials", "Trigger alert"],
    "Scammer": ["Deploy OpenCanary services", "Provide fake user data", "Monitor phishing attempt"],
    "Organized Cybercriminal": ["Fake payment page", "Decoy database with tracking", "Deploy financial fraud honeypot"],
    "Hacktivist": ["Simulate fake DDoS countermeasures", "Fake traffic shaping alerts", "Log and track botnet behavior"],
}

def deploy_deception(attacker_type):
    """Select and apply deception strategy."""
    deception = random.choice(deception_responses.get(attacker_type, ["No deception available"]))
    return deception
