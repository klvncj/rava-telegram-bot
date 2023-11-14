# Telegram News and Chat Bot with ChatGPT - Rava v2

Welcome to the Telegram News and Chat Bot repository! This Python-based Telegram bot is designed to provide users with the latest tech news, country-specific news, and international headlines. Additionally, it can engage in casual conversation when not responding to specific commands, thanks to the integration of ChatGPT.

## Getting Started

### Prerequisites

Before running the bot, make sure you have the following installed:

- Python 3.x
- `python-telegram-bot` library
- OpenAI GPT-3 API key (for ChatGPT integration)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/klvncj/rava-telegram-bot.git
    cd telegram-news-chat-bot
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Telegram Bot on [BotFather](https://core.telegram.org/bots#botfather) and obtain the bot token.

4. Obtain your OpenAI GPT-3 API key from the OpenAI platform.

5. Update the  file with your Telegram Bot token and OpenAI API key:

    ```python
    # bot.py

    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
    api_key  = 'YOUR_OPENAI_API_KEY'
    ```

### Usage

Run the bot using the following command:

```bash
python bot.py
```

Now, you can interact with the bot on Telegram. Start a chat with your bot and use the following commands:

- `/tech`: Get the latest tech news.
- `/naija`: Get the latest news for a specific country (currently only offers Nigerian news 😛).
- `/news`: Get international headlines.

When not using commands, the bot will engage in casual conversation, thanks to the integrated ChatGPT.

## Contributors

- Kelvin - ckelvin196@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the developers of the `python-telegram-bot` library.
- OpenAI for providing the amazing ChatGPT model.

Feel free to contribute, report issues, or suggest improvements!
