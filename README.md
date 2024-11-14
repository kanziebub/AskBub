# AskBub
Originally created to be a finetuned question andwering bot for an e-sport tournament Discord, but I gave up getting coherent results from the simple Information Retrieval query system. Now it's just there to entertain people with how delusional the free trial model is.

## Getting Started
1. Make sure you have set up a Discord Bot from the Discord Developer Portal and a Cohere account.
2. After cloning the repository, make a `.env` file in the root of the directory, it should have these variables set up:
   - `DISCORD_BOT_TOKEN=<your-bot-token>`
   - `COHERE_API_KEY=<your-api-key>`
3. You should have Python and pip installed. Run `pip install -r requirements.txt` in the root directory. It would be preferrable if you set up an environment first.
4. Lastly, simply run `python bot.py` and your bot should be online. This is a local login, so if you stop the program from running, your bot will go offline.
