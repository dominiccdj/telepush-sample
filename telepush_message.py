import requests

def send_telegram_message(token, message):
    url = f"https://telepush.dev/api/messages/{token}"
    payload = {"text": message}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status Code: {response.status_code}, Error: {response.text}")

# Example usage
if __name__ == "__main__":
    # Replace with your Telepush token
    telepush_token = "your-telepush-token-here"
    
    # Replace with your desired message
    message_content = "Hello! This is a test message sent via Telepush."

    send_telegram_message(telepush_token, message_content)
