import telebot
import requests

API_KEY = 'Your API Key'
bot = telebot.TeleBot(API_KEY)

API_URL = "https://api.coingecko.com/api/v3/simple/price"
headers = {"accept": "application/json"}

def get_prices(coin_ids, vs_currency='usd'):
    params = {
        'ids': ','.join(coin_ids),
        'vs_currencies': vs_currency
    }
    response = requests.get(API_URL, headers=headers, params=params)
 #   print("Request URL:", response.url)  # Print the request URL
 #   print("Response status code:", response.status_code)  # Print the response status code
 #   print("Response text:", response.text)  # Print the response text
    if response.status_code == 200:
        data = response.json()
        return data
    else:
     #   print(f"Failed to fetch prices. Status code: {response.status_code}")
     #   print(f"Response text: {response.text}")
        return None


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    help_text = 'Hi this is crypto price bot.\nGive these commands to get crypto prices:\n\n'
    help_text += '\n'.join([f'/{coin_id.lower()} - {coin_name}' for coin_id, coin_name in COIN_INFO.items()])
    bot.send_message(chat_id=message.chat.id, text=help_text)

@bot.message_handler(func=lambda message: message.text.startswith('/'))
def get_coin_price(message):
    coin_id = message.text.lstrip('/')
    if coin_id.lower() not in COIN_INFO:
        bot.send_message(chat_id=message.chat.id, text='Invalid coin ID')
        return

    prices = get_prices([coin_id.lower()])
    if prices:
        price = prices.get(coin_id.lower(), {}).get('usd')
        if price is not None:
            coin_name = COIN_INFO[coin_id.lower()]
            response = f"{coin_name} - ${price:.2f}"
            bot.send_message(chat_id=message.chat.id, text=response)
        else:
            bot.send_message(chat_id=message.chat.id, text=f"Price for {coin_id.upper()} not available")
    else:
        bot.send_message(chat_id=message.chat.id, text=f"Failed to fetch price for {coin_id.upper()}")

COIN_INFO = {
    'bitcoin': 'Bitcoin',
    'ethereum': 'Ethereum',
    'tether': 'Tether',
    'binancecoin': 'Binance Coin',
    'solana': 'Solana',
    'usdc': 'USD Coin',
    'xrp': 'XRP',
    'dogecoin': 'Dogecoin',
    'toncoin': 'Toncoin',
    'cardano': 'Cardano',
    'avalanche': 'Avalanche',
    'shibainu': 'Shiba Inu',
    'bitcoincash': 'Bitcoin Cash',
    'polkadot': 'Polkadot',
    'tron': 'TRON',
    'chainlink': 'Chainlink',
    'polygon': 'Polygon',
    'internetcomputer': 'Internet Computer',
    'litecoin': 'Litecoin',
    'nearprotocol': 'NEAR Protocol',
    'unussadleo': 'UNUS SED LEO',
    'dai': 'Dai',
    'uniswap': 'Uniswap',
    'ethereumclassic': 'Ethereum Classic',
    'firstdigitalusd': 'First Digital USD',
    'aptos': 'Aptos',
    'stacks': 'Stacks',
    'mantle': 'Mantle',
    'cosmos': 'Cosmos',
    'arbitrum': 'Arbitrum',
    'cronos': 'Cronos',
    'bittensor': 'Bittensor',
    'filecoin': 'Filecoin',
    'stellar': 'Stellar',
    'okb': 'OKB',
    'immutable': 'Immutable',
    'render': 'Render',
    'hedera': 'Hedera',
    'vechain': 'VeChain',
    'thegraph': 'The Graph',
    'kaspa': 'Kaspa',
    'maker': 'Maker',
    'injective': 'Injective',
    'optimism': 'Optimism',
    'pepe': 'Pepe',
    'thetanetwork': 'Theta Network',
    'monero': 'Monero',
    'fantom': 'Fantom',
    'thorchain': 'THORChain',
    'lido': 'Lido DAO'
}


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
