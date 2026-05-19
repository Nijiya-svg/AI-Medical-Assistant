import openai
import os

def analyze_symptoms(symptoms):
    # Simple keyword matching for demo
    symptoms_lower = symptoms.lower()
    if 'fever' in symptoms_lower and 'cough' in symptoms_lower:
        return 'Common Cold or Flu', 'General Physician'
    elif 'skin' in symptoms_lower and 'rash' in symptoms_lower:
        return 'Skin Allergy', 'Dermatologist'
    elif 'headache' in symptoms_lower:
        return 'Migraine or Tension Headache', 'Neurologist'
    else:
        return 'General Checkup Needed', 'General Physician'

    # For OpenAI integration (uncomment if API key is set)
    # openai.api_key = os.getenv('OPENAI_API_KEY')
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=f"Analyze these symptoms: {symptoms}. Predict possible condition and recommend specialist.",
    #     max_tokens=100
    # )
    # result = response.choices[0].text.strip()
    # # Parse result to condition and specialist
    # return result, 'General Physician'  # Placeholder