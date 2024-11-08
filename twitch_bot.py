import time
import random
from twitchio.ext import commands

# Authentication and Channel Details
BOT_TOKEN = 'your_oauth_token'  # Replace with your bot's OAuth token
USERNAME = 'your_username'  # Replace with your bot's username
CHANNEL = 'kai_cenat'  # Channel you want to chat in

# Base messages with placeholders for easy variation
BASE_MESSAGES = [
    "Yo Kai, let Quavo shine! The side characters gotta chill for a sec! {}",
    "This is rare! Let Quavo have the spotlight, for real! {}",
    "Kai, we need more Quavo time—keep the side talk low key! {}",
    "Quavo’s in the building! Side characters stepping back, let him speak! {}",
    "Quavo here with Kai? Iconic! Side convos need to pause for the main act! {}"
]

# List of emojis and symbols to rotate for variation
EMOJI_VARIANTS = ["🔥", "👀", "💯", "🙌", "🚀", "✨"]


class TwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(token=BOT_TOKEN, prefix='!', initial_channels=[CHANNEL])

    async def event_ready(self):
        print(f'Logged in as {USERNAME} in Kai Cenat\'s chat!')

    async def post_dynamic_messages(self):
        while True:
            # Select a base message and add a random emoji for variation
            base_message = random.choice(BASE_MESSAGES)
            emoji = random.choice(EMOJI_VARIANTS)
            message = base_message.format(emoji)

            # Send message to Twitch chat
            await self.get_channel(CHANNEL).send(message)

            # Small delay for high-frequency posting, varies between 5-10 seconds
            delay = random.uniform(5, 10)
            time.sleep(delay)


bot = TwitchBot()
bot.run()
