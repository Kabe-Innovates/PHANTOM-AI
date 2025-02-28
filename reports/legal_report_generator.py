# reports/legal_report_generator.py
import json
from ai_model.legal_report_ai import generate_legal_report
from email_sender.email_sender import send_email

def generate_and_send_reports():
    """Fetch predictions and send formatted legal reports via email."""
    try:
        # Load the predictions from the legal_database.json file
        with open('database.json', 'r') as file:
            predictions = json.load(file)

        for prediction in predictions:
            title = prediction['title']
            predicted_class = prediction['predicted_class']
            
            # Generate the legal report based on title and predicted class
            legal_report = generate_legal_report(title, predicted_class)

            # Send the legal report via email
            recipient_email = "recipient@example.com"  # Replace with the actual recipient email
            subject = f"Legal Report: {title}"
            send_email(recipient_email, subject, legal_report)
    
    except Exception as e:
        print(f"Error generating or sending report: {e}")

if __name__ == "__main__":
    generate_and_send_reports()
