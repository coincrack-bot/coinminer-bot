import requests
import time

TOKEN = "7663286233:AAHDys4VjaAJeyvYzV2SSqOIEY8TRv6nC6c"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates(offset=None):
    url = f"{API_URL}/getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates["result"]:
            message = update["message"]
            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            # Basic bot response
            if text == "/start":
                send_message(chat_id, "Welcome to Indian Miner Bot! 🚀")
            else:
                send_message(chat_id, f"You said: {text}")

            offset = update["update_id"] + 1
        time.sleep(1)

if __name__ == "__main__":
    main()
