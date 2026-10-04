import pyautogui
import pyperclip
import time
import re
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=""
)

MY_NAME = "Ashwin Patil"

# Open WhatsApp
pyautogui.click(1098, 1052)
time.sleep(2)

last_replied_message = ""

while True:

    # -------------------------------
    # SELECT WHATSAPP CHAT
    # -------------------------------
    pyautogui.click(728, 204)
    pyautogui.moveTo(728, 204, duration=0.3)
    pyautogui.mouseDown()
    pyautogui.moveTo(1843, 919, duration=1)
    pyautogui.mouseUp()

    time.sleep(0.3)

    # Copy
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    chat_history = pyperclip.paste().strip()

    if not chat_history:
        time.sleep(1)
        continue

    print("\n---------------------------")
    print(chat_history)
    print("---------------------------")

    # -------------------------------
    # FIND ALL MESSAGES
    # -------------------------------
    pattern = r"\[(\d{1,2}:\d{2}\s?[AP]M,\s*[^]]+)\]\s*([^:]+):"

    matches = list(re.finditer(pattern, chat_history))

    if not matches:
        print("Could not detect messages.")
        time.sleep(1)
        continue

    # -------------------------------
    # GET LAST MESSAGE
    # -------------------------------
    last_match = matches[-1]

    sender_name = last_match.group(2).strip()

    # Text of last message
    last_message_start = last_match.end()

    if len(matches) > 1:
        previous_match_end = matches[-2].end()
        last_message = chat_history[last_message_start:]
    else:
        last_message = chat_history[last_message_start:]

    last_message = last_message.strip()

    print("Last sender:", sender_name)
    print("Last message:", last_message)

    # -------------------------------
    # IF LAST MESSAGE IS MINE
    # -------------------------------
    if sender_name.lower() == MY_NAME.lower():

        print("Last message is from Ashwin Patil.")
        print("WAITING FOR SENDER...")

        time.sleep(2)
        continue

    # -------------------------------
    # DON'T REPLY TWICE
    # -------------------------------
    current_message_id = (
        sender_name + "|" + last_message
    )

    if current_message_id == last_replied_message:

        print("Already replied to this message.")
        time.sleep(2)
        continue

    # -------------------------------
    # SENDER SENT LAST MESSAGE
    # -------------------------------
    print("SENDER SENT LAST MESSAGE!")
    print("Generating AI reply...")

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a person named Ashwin Patil who speaks "
                    "Hindi and English. You are from India. "
                    "Analyze the chat history and reply naturally "
                    "like Ashwin Patil. "
                    "Reply like a normal person having a conversation. "
                    "Maximum 3 lines. "
                    "Do not mention AI or ChatGPT."
                )
            },
            {
                "role": "user",
                "content": chat_history
            }
        ]
    )

    response = completion.choices[0].message.content.strip()

    print("AI RESPONSE:")
    print(response)

    # -------------------------------
    # SEND REPLY
    # -------------------------------
    pyautogui.click(955, 975)
    time.sleep(0.3)

    pyperclip.copy(response)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.3)

    pyautogui.press("enter")

    print("Reply sent!")

    # Remember this message
    last_replied_message = current_message_id

    # Wait before checking again
    time.sleep(2)
