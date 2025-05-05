from nltk.chat.util import Chat, reflections
import re

# Dummy order database
orders = {
    "111": "Your order #111 is shipped.",
    "222": "Your order #222 is delivered.",
    "333": "Your order #333 is being processed."
}

# Product categories list
products = ['Electronics', 'Books', 'Clothes', 'Home Appliances']

# Patterns and replies
pairs = [
    (r'(?i)hi|hello|hey', ["Hello! How can I help you?"]),
    (r'(?i)how are you\??', ["I'm good! How can I assist?"]),
    (r'(?i)what is your name\??', ["I'm ShopEase Bot!"]),
    (r'(?i)products|product categories', [f"We offer: {', '.join(products)}"]),
    (r'(?i)(.*)place an order(.*)',['You can place an order by visiting our website,selecting a product, and proceeding to checkout.']),
    (r'(?i)track order (\d+)', ["#track_order"]),
    (r'(?i)(.*)return policy(.*)',['Returns are accepted within 30 days of purchase with a valid receipt.']),
    (r'(?i)(.*)contact(.*)', ['You can contact us via our website chat, email support@shopease.com, or call 1-800-123-4567.']),
    (r'(?i)(.*)business hours(.*)',['Our support team is available 9 AM to 5 PM, Monday to Friday.']),
    (r'(?i)thanks|thank you', ["You're welcome!"]),
    (r'(.*)', ["Sorry, I didn’t understand that."])
]

# Custom function to handle order tracking
def get_response(user_input):
    match = re.search(r'(?i)track order (\d+)', user_input)
    if match:
        order_id = match.group(1)
        return orders.get(order_id, f"No info found for order #{order_id}.")
    else:
        return bot.respond(user_input)

# Chat instance
bot = Chat(pairs, reflections)

# Chat loop
def chat():
    print("Welcome to ShopEase Support! Type 'quit' to exit.")
    while True:
        user = input("You: ")
        if user.lower() == 'quit':
            print("Bot: Bye! Have a nice day!")
            break
        print("Bot:", get_response(user))

# Run chatbot
if __name__ == "__main__":
    chat()





# ### 🔹 **Basic Understanding**

# 1. **Q: What is the purpose of the `Chat` class in this code?**
#    **A:** It is used to create a rule-based chatbot that replies based on predefined pattern–response pairs.

# 2. **Q: What is the use of the `reflections` variable?**
#    **A:** It’s a dictionary that maps first-person pronouns to second-person (like "I" to "you") to make conversations more natural, though we aren’t customizing it here.

# 3. **Q: What does the `pairs` list represent?**
#    **A:** It contains tuples of regex patterns and their corresponding bot responses. The chatbot uses this to match user input and reply accordingly.

# ---

# ### 🔹 **Regex and Input Handling**

# 4. **Q: What does the pattern `r'(?i)track order (\d+)'` mean?**
#    **A:** It matches phrases like “track order 123”. `(?i)` makes it case-insensitive, and `(\d+)` captures the digits (order number).

# 5. **Q: Why are `.*` used in some patterns like `(.*)place an order(.*)`?**
#    **A:** To allow the phrase “place an order” to appear anywhere in the sentence, ignoring the words before and after.

# 6. **Q: What is the purpose of the `get_response()` function?**
#    **A:** It checks if the user input is about order tracking and handles it manually using regex. Otherwise, it uses the chatbot’s default logic.

# ---

# ### 🔹 **Data and Response Logic**

# 7. **Q: How is order tracking implemented in the code?**
#    **A:** Through a dictionary named `orders` that maps order IDs to their status. The bot uses regex to extract the ID and fetch the response from the dictionary.

# 8. **Q: What happens if a user enters an unknown order ID?**
#    **A:** The bot responds with “No info found for order #<id>”.

# 9. **Q: How does the bot respond to unknown or unrecognized input?**
#    **A:** It uses the fallback rule `(.*)` and responds with “Sorry, I didn’t understand that.”

# ---

# ### 🔹 **Chat Loop and Execution**

# 10. **Q: What is the purpose of `if __name__ == "__main__":`?**
#     **A:** It ensures that the chatbot runs only when the script is executed directly, not when it is imported.

# 11. **Q: How can the user exit the chatbot?**
#     **A:** By typing “quit”, which ends the chat loop and exits the program.

# 12. **Q: What will happen if the user types 'Hi'?**
#     **A:** The bot responds with “Hello! How can I help you?” based on the matching regex pattern.

# ---

# ### 🔹 **Extension/Conceptual**

# 13. **Q: How can you add more product categories to the bot?**
#     **A:** By appending to the `products` list. It will automatically update in the bot’s response.

# 14. **Q: How can this chatbot be improved to understand more natural language?**
#     **A:** By integrating NLP tools like spaCy or transformers, or by using a ML/DL-based chatbot model.

# 15. **Q: Can this chatbot remember the user's previous messages?**
#     **A:** No. It is stateless — each input is handled independently.

# ---

# Would you like me to format this into a PDF-style document or oral-response format?
