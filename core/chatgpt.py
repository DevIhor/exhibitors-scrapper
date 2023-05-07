import openai


def get_chatgpt_response(
        request_text: str
) -> str:
    """
    Search for response using ChatGPT
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": request_text},
        ]
    )
    return "".join([choice.message.content for choice in response.choices])
