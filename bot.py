import openai
import requests
from telegram import Update
from telegram.ext import ContextTypes,Application,CommandHandler,MessageHandler,filters

TOKEN = '##############################################' ## Add your own telegram bot api token here
BOT = '@your-bot-username'
api_key = "############################################" ## Add your own openai api key here
newsapi_key = "########################################"
openai.api_key = api_key

## NEWS REQUESTS 
def getTech():
    response = requests.get(f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={newsapi_key}')
    news = response.json()
    articles = news.get('articles', [])
    if not articles:
        return 'No Article found'

    news_list = []
    news_list.append('Hello Kelvin , This is the Tech news of the week')
    for article in articles:
        title = article.get('title', 'N/A')
        url = article.get('url', '#')
        news_list.append(f"{title}\n{url}\n")

    return '\n'.join(news_list)

def getNaija():
    base_url = f'https://newsapi.org/v2/top-headlines?country=ng&apiKey={newsapi_key}'
    params = {
        'apiKey': newsapi_key,
        'pageSize': 10,  
    }

    response = requests.get(base_url, params=params)
    news_data = response.json()
    articles = news_data.get('articles', [])
    if not articles:
        return 'No Article found'

    news_list = []
    news_list.append('Hello Kelvin , This is the Nigerian news ')
    for article in articles:
        title = article.get('title', 'N/A')
        published = article.get('publishedAt', 'N/A')
        description = article.get('description', 'N/A')
        url = article.get('url', '#')
        news_list.append(f"{title}\n{url}\n")

    return '\n'.join(news_list)

def getHeadlines():
    response = requests.get(
        f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi_key}', )
    news = response.json()
    articles = news.get('articles', [])
    if not articles:
        return 'No Article found'

    news_list = []
    news_list.append('Hello Kelvin , This is the Healines of the week')
    for article in articles:
        title = article.get('title', 'N/A')
        url = article.get('url', '#')
        news_list.append(f"{title}\n{url}\n")

    return '\n'.join(news_list)


##COMMAND CENTER 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hello I am Rava - Replicated Advanced Virtual Assistant , How may I be of service to you now')


async def headline_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getHeadlines())


async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Chat History is Currently not available')


async def tech_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getTech())


async def naija_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(getNaija())


# HANDLEING USER MESSAGE
def handle_response(text: str):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": text}])
    text = completion.choices[0].message.content
    return text


async def handle_mesage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User({update.message.chat_id}) in {message_type} : {text}')
    if message_type == 'group':
        if BOT in text:
            new_text = text.replace(BOT,'').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


async  def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused the following error {context.error}')

if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('news', headline_command))
    app.add_handler(CommandHandler('naija', naija_command))
    app.add_handler(CommandHandler('tech', tech_command))
    app.add_handler(CommandHandler('chats', history_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT,handle_mesage))


    #Errors
    app.add_error_handler(error)
    print('Pooling...')
    app.run_polling(poll_interval=3)
