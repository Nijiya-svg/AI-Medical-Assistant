import re

SYMPTOM_RESPONSES = [
    (['headache', 'vomit'], "Headache combined with vomiting may indicate a migraine or tension issue. Rest, stay hydrated, and avoid bright lights; if symptoms are severe or persistent, please consult a doctor."),
    (['headache', 'migraine'], "For headaches or migraines, a general physician or neurologist can help evaluate triggers and treatment options."),
    (['fever', 'cough'], "These symptoms may indicate a viral infection. Rest, stay hydrated, and consider seeing a general physician if they persist."),
    (['fever', 'cold'], "Fever with cold symptoms may be a viral infection. Keep warm, drink fluids, and see a doctor if your temperature stays high."),
    (['throat', 'sore'], "A sore throat can be caused by a cold or infection. Drink warm fluids and rest; if pain persists, consult an ENT or general physician."),
    (['stomach', 'pain'], "Stomach pain may come from indigestion or infection. Try light meals and hydration; see a gastroenterologist if symptoms worsen."),
    (['nausea', 'vomit'], "Nausea and vomiting can result from an infection or digestion issue. Stay hydrated and seek medical advice if it continues."),
    (['back', 'pain'], "Back pain may need a physiotherapist or orthopedist evaluation if it continues."),
    (['skin', 'allergy'], "This looks like a skin allergy. A dermatologist can help with diagnosis and treatment."),
    (['chest', 'pain'], "Chest pain is serious. Please consult a healthcare professional immediately if you are experiencing chest discomfort."),
]

HELP_MESSAGES = {
    'appointment': "To book an appointment, open the doctor list and select a specialist that matches your needs. You can also tell me your symptoms and I can suggest the right type of doctor.",
    'book': "To book an appointment, open the doctor list and select a specialist that matches your needs. You can also tell me your symptoms and I can suggest the right type of doctor.",
    'symptom': "Please describe your symptoms clearly. Mention where you feel it, how long it has lasted, and whether it is mild or severe.",
    'doctor': "You can view doctors by specialization and available timings in the doctor list. Tell me what type of doctor you need and I will suggest one.",
    'help': "I can help with basic health guidance, appointment booking steps, and recommending what specialist to see. Please describe your symptoms or ask how to book an appointment.",
}

GREETING_RESPONSES = [
    "Hello! I’m your healthcare assistant. Tell me your symptoms or ask about appointments.",
    "Hi there! I can help with symptom guidance or doctor appointment suggestions.",
]

THANK_YOU_RESPONSES = [
    "You’re welcome! If you have more questions, feel free to ask.",
    "Glad to help. Let me know if you need anything else.",
]

DEFAULT_RESPONSE = (
    "I’m here to help with medical questions. Please describe your symptoms, ask how to book an appointment, "
    "or ask which specialist you should see."
)


def get_chat_response(message):
    message_lower = (message or '').strip().lower()
    if not message_lower:
        return "Please type a question or describe your symptoms so I can assist you."

    if re.search(r'\b(hi|hello|hey|good morning|good evening|greetings)\b', message_lower):
        return GREETING_RESPONSES[0]

    if re.search(r'\b(thank|thanks|thank you)\b', message_lower):
        return THANK_YOU_RESPONSES[0]

    if re.search(r'\b(what do you do|what is your job|who are you|how can you help)\b', message_lower):
        return "I’m an AI medical assistant. I can help you understand symptoms, suggest the right doctor type, and guide you toward booking an appointment."

    for keyword, answer in HELP_MESSAGES.items():
        if keyword in message_lower:
            return answer

    for keywords, answer in SYMPTOM_RESPONSES:
        if all(term in message_lower for term in keywords):
            return answer

    for keywords, answer in SYMPTOM_RESPONSES:
        if any(term in message_lower for term in keywords):
            return answer

    if re.search(r'\b(solution|treatment|remedy|fix|what should i do|how to treat)\b', message_lower):
        return (
            "If you describe your symptoms clearly, I can suggest the next steps or the right specialist to see. "
            "For now, make sure to rest and stay hydrated, and consult a doctor if your symptoms persist."
        )

    return DEFAULT_RESPONSE
