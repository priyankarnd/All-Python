from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

# Simple rule-based chatbot
def simple_chatbot(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm just a simple chatbot. How can I assist you?"

@app.post("/chatbot/")
async def chatbot_endpoint(user_message: str = Form(...)):
    response = simple_chatbot(user_message)
    return {"message": response}

