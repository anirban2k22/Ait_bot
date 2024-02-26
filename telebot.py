import google.generativeai as genai
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Set up the generative model and other configurations
genai.configure(api_key="AIzaSyDraA9X1rWIm8PZdOOt_jQVn0QAd5OjzRo")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Your Telegram Bot Token obtained from the BotFather
TELEGRAM_BOT_TOKEN = "6341178995:AAFtiqDChgf7sw_52ebi0O4fXdRK6veNuSk"

# Create an instance of the Telegram bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the user's message
    user_message = update.message.text

    # Process the user's message using the predefined conditions
    user_input = user_message.lower().replace(" ", "").replace("?", "").replace(",", "").replace(".", "").replace("/", "")

    if user_input == "whereisatriainstituteoftechnology":
        update.message.reply_text("Bot: Atria Institute of Technology is in Anandnagar, Hebbal, Bangalore, India.")
    elif user_input == "thankyou":
        update.message.reply_text("Bot: You're welcome!")
    elif user_input in ["hii", "hello"]:
        update.message.reply_text("Bot: Hello!")
    elif user_input == "goodmorning":
        update.message.reply_text("Bot: Good Morning!")
    elif user_input == "goodevening":
        update.message.reply_text("Bot: Good Evening!")
    elif user_input == "bye":
        update.message.reply_text("Bot: Bye, Thank you for talking with me.")
    
    # ... (other predefined conditions)

    # If none of the predefined conditions are met, use the generative model
    else:
        # Process the user's message using the generative model
        response = model.generate_content([user_message])
        # Send the generated response back to the user
        update.message.reply_text("Bot: " + response.text)

# Set up the Telegram bot updater and dispatcher
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add a handler for regular text messages
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
