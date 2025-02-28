from transformers import pipeline

# Load a pre-trained GPT-2 model for text generation (you can switch this out with any other model from HuggingFace)
generator = pipeline('text-generation', model='gpt2')

# Sample IPC mapping for demonstration purposes
IPC_MAPPING = [
    {
        "attack_type": "Phishing",
        "violation": "Section 66C - Identity Theft, Section 66D - Cheating by Personation, Section 420 IPC - Cheating and dishonestly inducing delivery of property",
        "penalty": "3 years imprisonment + fine up to ₹1 lakh (Section 66C & 66D), Up to 7 years imprisonment + fine (Section 420 IPC)"
    },
    {
        "attack_type": "SQL Injection",
        "violation": "Section 43 - Unauthorized Access, Section 70 - Protected System",
        "penalty": "Compensation up to ₹5 lakh (Section 43), Up to 10 years imprisonment + fine (Section 70)"
    },
    {
        "attack_type": "Denial of Service (DoS)",
        "violation": "Section 66 - Hacking, Section 70 - Protected System",
        "penalty": "Imprisonment up to 3 years + fine up to ₹5 lakh (Section 66), Up to 10 years imprisonment + fine (Section 70)"
    },
     {
        "attack_type": "Phishing",
        "violation": "Section 66C - Identity Theft, Section 66D - Cheating by Personation, Section 420 IPC - Cheating and dishonestly inducing delivery of property",
        "penalty": "3 years imprisonment + fine up to ₹1 lakh (Section 66C & 66D), Up to 7 years imprisonment + fine (Section 420 IPC)"
    },
    {
        "attack_type": "SQL Injection",
        "violation": "Section 43 - Unauthorized Access, Section 70 - Protected System",
        "penalty": "Compensation up to ₹5 lakh (Section 43), Up to 10 years imprisonment + fine (Section 70)"
    },
    {
        "attack_type": "Denial of Service (DoS)",
        "violation": "Section 66 - Hacking, Section 70 - Protected System",
        "penalty": "Imprisonment up to 3 years + fine up to ₹5 lakh (Section 66), Up to 10 years imprisonment + fine (Section 70)"
    },
    {
        "attack_type": "Cyber Terrorism",
        "violation": "Section 66F - Cyber Terrorism",
        "penalty": "Imprisonment up to life"
    },
    {
        "attack_type": "Identity Theft",
        "violation": "Section 66C - Identity Theft, Section 419 IPC - Cheating by personation",
        "penalty": "3 years imprisonment + fine up to ₹1 lakh (Section 66C), Up to 3 years imprisonment + fine (Section 419 IPC)"
    },
    {
        "attack_type": "Cheating by Personation",
        "violation": "Section 66D - Cheating by Personation, Section 419 IPC - Cheating by personation",
        "penalty": "3 years imprisonment + fine up to ₹1 lakh (Section 66D), Up to 3 years imprisonment + fine (Section 419 IPC)"
    },
    {
        "attack_type": "Publishing Obscene Material",
        "violation": "Section 67 - Publishing Obscene Material, Section 67A - Publishing sexually explicit act",
        "penalty": "5 years imprisonment + fine up to ₹10 lakh (Section 67), 7 years imprisonment + fine up to ₹5 lakh (Section 67A)"
    },
    {
        "attack_type": "Voyeurism",
        "violation": "Section 66E - Violation of Privacy, Section 354C IPC - Voyeurism",
        "penalty": "3 years imprisonment + fine up to ₹2 lakh (Section 66E), 1-3 years imprisonment + fine (Section 354C IPC)"
    },
    {
        "attack_type": "Cyber Stalking",
        "violation": "Section 354D IPC - Stalking",
        "penalty": "Up to 3 years imprisonment for first offence, up to 5 years for second offence"
    },
    {
        "attack_type": "Theft of Computer Hardware",
        "violation": "Section 379 IPC - Theft",
        "penalty": "Up to 3 years imprisonment + fine"
    },
    {
        "attack_type": "Password Theft for Fraud",
        "violation": "Section 420 IPC - Cheating and dishonestly inducing delivery of property, Section 66C - Identity Theft",
        "penalty": "Up to 7 years imprisonment + fine (Section 420 IPC), 3 years imprisonment + fine up to ₹1 lakh (Section 66C)"
    },
    {
        "attack_type": "Email Spoofing",
        "violation": "Section 463 IPC - Forgery",
        "penalty": "Up to 2 years imprisonment + fine"
    },
    {
        "attack_type": "Forgery in Cyberspace",
        "violation": "Section 465 IPC - Forgery",
        "penalty": "Up to 2 years imprisonment + fine"
    },
    {
        "attack_type": "Defamation via Email",
        "violation": "Section 499 IPC - Defamation",
        "penalty": "Up to 2 years imprisonment + fine"
    },
    {
        "attack_type": "Criminal Intimidation via Email",
        "violation": "Section 506 IPC - Punishment for criminal intimidation",
        "penalty": "Up to 2 years imprisonment + fine"
    },
    {
        "attack_type": "Copyright Infringement",
        "violation": "Section 63 Copyright Act - Offence of infringement of copyright or other rights conferred by this Act",
        "penalty": "Imprisonment up to 3 years + fine up to ₹2 lakh"
    },
    {
        "attack_type": "Data Breach",
        "violation": "Section 43A - Compensation for failure to protect data",
        "penalty": "Compensation as determined by the adjudicating officer"
    },
    {
       "attack_type": "Violation of Privacy",
        "violation": "Section 72 - Breach of confidentiality and privacy",
        "penalty": "Imprisonment for a term which may extend to two years, or with fine which may extend to one lakh rupees, or with both."
    }
    # Add other attack types and IPC sections here...
]

def generate_legal_report(title, predicted_class):
    """Generate a legal report based on title and predicted class using a simple Gen-AI model."""
    
    # Get today's date for the report
    report_date = '2025-03-01'  # Use today's date in real-time apps
    
    # Find the corresponding IPC section from the list
    ipc_section = "No IPC section available for this crime"
    for item in IPC_MAPPING:
        if item["attack_type"].lower() == predicted_class.lower():
            ipc_section = f"Violation: {item['violation']}\nPenalty: {item['penalty']}"
            break  # Exit the loop once a match is found

    # Simple input for Gen-AI model (you can customize this prompt to be more elaborate)
    prompt = f"Generate a legal report for the following incident: {predicted_class}. The cyber crime predicted is {predicted_class}. The corresponding IPC section is {ipc_section}."

    # Use the pre-trained GPT-2 model to generate the report text
    generated_report = generator(prompt, max_length=250, num_return_sequences=1)[0]['generated_text']

    # Clean the generated text by removing the prompt part from the output (just for cleanliness)
    generated_report = generated_report.replace(prompt, "").strip()

    # Format the legal report
    report = f"""
    Legal Report - Cyber Crime Case

    Date of Report: {report_date}

    Incident Title: {title}
    Predicted Crime Category: {predicted_class}

    Relevant IPC Section:
    {ipc_section}

    Generated Legal Text:
    {generated_report}

    Notes:
    - Ensure that the report is submitted to the local cybercrime authorities.
    - Further investigation is required to gather evidence regarding the criminal activities.
    - Take preventive measures as per the Indian Cyber Crime Prevention policy.

    Regards,
    Cyber Intelligence Team
    """
    
    return report
