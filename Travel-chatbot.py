import tkinter as tk
from tkinter import scrolledtext

def send_message():
    user_message = entry.get().strip()

    if user_message == "":
        return

    chat_area.insert(tk.END, "You: " + user_message + "\n")

    msg = user_message.lower()

    if "mysore" in msg:
        bot_reply = """
Places to Visit in Mysore

1. Mysore Palace
   Ticket Price: ₹100

2. Chamundi Hills
   Ticket Price: Free

3. Brindavan Gardens
   Ticket Price: ₹50

4. Mysore Zoo
   Ticket Price: ₹100

Hotels

1. Royal Orchid Metropole
   Price: ₹4500/night

2. Pai Vista Hotel
   Price: ₹3000/night

Estimated Trip Cost

Budget Trip: ₹4000 - ₹6000
Standard Trip: ₹8000 - ₹12000
Luxury Trip: ₹15000+
"""

    elif "goa" in msg:
        bot_reply = """
Places to Visit in Goa

1. Baga Beach
   Ticket Price: Free

2. Calangute Beach
   Ticket Price: Free

3. Fort Aguada
   Ticket Price: ₹50

4. Dudhsagar Falls
   Ticket Price: ₹400

Hotels

1. Beach Resort
   Price: ₹3500/night

2. Sea View Inn
   Price: ₹2500/night

Estimated Trip Cost

Budget Trip: ₹7000 - ₹10000
Standard Trip: ₹12000 - ₹18000
Luxury Trip: ₹25000+
"""

    elif "bangalore" in msg:
        bot_reply = """
Places to Visit in Bangalore

1. Lalbagh Botanical Garden
   Ticket Price: ₹30

2. Cubbon Park
   Ticket Price: Free

3. Bangalore Palace
   Ticket Price: ₹240

4. Vidhana Soudha
   Ticket Price: Free

Hotels

1. ITC Gardenia
   Price: ₹8000/night

2. Taj MG Road
   Price: ₹7000/night

Estimated Trip Cost

Budget Trip: ₹5000 - ₹8000
Standard Trip: ₹10000 - ₹15000
Luxury Trip: ₹25000+
"""

    elif "singapore" in msg:
        bot_reply = """
Places to Visit in Singapore

1. Marina Bay Sands
   Ticket Price: ₹1500

2. Gardens by the Bay
   Ticket Price: ₹1200

3. Sentosa Island
   Ticket Price: ₹2000

4. Universal Studios Singapore
   Ticket Price: ₹5000

5. Merlion Park
   Ticket Price: Free

Hotels

1. Marina Bay Sands Hotel
   Price: ₹25000/night

2. Carlton Hotel Singapore
   Price: ₹12000/night

Estimated Trip Cost

Budget Trip: ₹50000+
Standard Trip: ₹80000+
Luxury Trip: ₹150000+
"""

    elif "hi" in msg or "hello" in msg:
        bot_reply = """
Hello!

Available Destinations:
• Mysore
• Goa
• Bangalore
• Singapore

Type a destination name to get details.
"""

    else:
        bot_reply = """
Sorry!

Available Destinations:
• Mysore
• Goa
• Bangalore
• Singapore
"""

    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_area.see(tk.END)

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Travel Guide Chatbot")
root.geometry("800x600")

title_label = tk.Label(
    root,
    text="🌍 Travel Guide Chatbot",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    width=90,
    height=25,
    font=("Arial", 11)
)
chat_area.pack(padx=10, pady=10)

chat_area.insert(
    tk.END,
    "Bot: Welcome! Where would you like to travel?\n\n"
)

entry = tk.Entry(
    root,
    width=80,
    font=("Arial", 12)
)
entry.pack(pady=5)

send_button = tk.Button(
    root,
    text="Send",
    font=("Arial", 12),
    command=send_message
)
send_button.pack(pady=5)

root.mainloop()