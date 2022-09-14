import telebot
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


API_KEY = ''    #paste your API key here
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
  msg = 'Hi this is crypto price bot.\nGive these commands to get cypto prices of these coins.\nFor\nBitcoin  /btc\nEthereum  /eth\nLitecoin  /ltc\nBinanceCoin   /bnb\nRipple   /xrp\nCardano   /ada\nSolana   /sol\nPolakadot   /dot\nDogeCoin   /doge\nShib   /shib\nTron   /trx\nCosmos   /atom\nChainLink   /link\nAvax   /avax\nMatic   /matic\nNear   /near\nApeCoin   /ape\nMonero   /xmr\nMana   /mana\nSand   /sand\nAxs   /axs\nLunc   /lunc\nAave   /aave\nFor help   /help'
  bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['help'])
def help(message):
  msg = 'Hi this is crypto price bot.\nGive these commands to get cypto prices of these coins.\nFor\nBitcoin  /btc\nEthereum  /eth\nLitecoin  /ltc\nBinanceCoin   /bnb\nRipple   /xrp\nCardano   /ada\nSolana   /sol\nPolakadot   /dot\nDogeCoin   /doge\nShib   /shib\nTron   /trx\nCosmos   /atom\nChainLink   /link\nAvax   /avax\nMatic   /matic\nNear   /near\nApeCoin   /ape\nMonero   /xmr\nMana   /mana\nSand   /sand\nAxs   /axs\nLunc   /lunc\nAave   /aave\nFor help   /help'
  bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['btc'])
def bitcoin(message):
  btc = cg.get_price(ids='bitcoin', vs_currencies='usd')
  bitcoin = 'Bitcoin   ' + '$ ' + str(btc['bitcoin']['usd']) 
  bot.send_message(message.chat.id, bitcoin)


@bot.message_handler(commands = ['eth'])
def ethereum(message):
  eth = cg.get_price(ids='ethereum', vs_currencies='usd')
  ethereum = 'Ethereum   ' +'$ ' + str(eth['ethereum']['usd'])  
  bot.send_message(message.chat.id, ethereum)


@bot.message_handler(commands = ['ltc'])
def litecoin(message):
  ltc = cg.get_price(ids='litecoin', vs_currencies='usd')
  litecoin = 'Litecoin   ' +'$ ' + str(ltc['litecoin']['usd'])  
  bot.send_message(message.chat.id, litecoin)


@bot.message_handler(commands = ['bnb'])
def binancecoin(message):
  bnb = cg.get_price(ids='binancecoin', vs_currencies='usd')
  binancecoin = 'Binancecoin   ' +'$ ' + str(bnb['binancecoin']['usd'])  
  bot.send_message(message.chat.id, binancecoin)


@bot.message_handler(commands = ['xrp'])
def ripple(message):
  xrp = cg.get_price(ids='ripple', vs_currencies='usd')
  ripple = 'Ripple   ' +'$ ' + str(xrp['ripple']['usd'])  
  bot.send_message(message.chat.id, ripple)


@bot.message_handler(commands = ['ada'])
def cardano(message):
  ada = cg.get_price(ids='cardano', vs_currencies='usd')
  cardano = 'Cardano   ' +'$ ' + str(ada['cardano']['usd'])   
  bot.send_message(message.chat.id, cardano)


@bot.message_handler(commands = ['sol'])
def solana(message):
  sol = cg.get_price(ids='solana', vs_currencies='usd')
  solana = 'Solana   ' +'$ ' + str(sol['solana']['usd'])  
  bot.send_message(message.chat.id, solana)


@bot.message_handler(commands = ['dot'])
def polkadot(message):
  dot = cg.get_price(ids='polkadot', vs_currencies='usd')
  polkadot = 'Polkadot   ' +'$ ' + str(dot['polkadot']['usd'])  
  bot.send_message(message.chat.id, polkadot)


@bot.message_handler(commands = ['doge'])
def doge(message):
  doge = cg.get_price(ids='dogecoin', vs_currencies='usd')
  dogecoin = 'DogeCoin   ' +'$ ' + str(doge['dogecoin']['usd'])  
  bot.send_message(message.chat.id, dogecoin)


@bot.message_handler(commands = ['shib'])
def shib(message):
  shib = cg.get_price(ids='shiba-inu', vs_currencies='usd')
  shibainu = 'Shib   ' +'$ ' + '{:.8f}'.format(float(str(shib['shiba-inu']['usd'])))   #"{:.8f}".format(float(""))
  bot.send_message(message.chat.id, shibainu)


@bot.message_handler(commands = ['trx'])
def tron(message):
  trx = cg.get_price(ids='tron', vs_currencies='usd')
  tron = 'Tron   ' +'$ ' + str(trx['tron']['usd'])  
  bot.send_message(message.chat.id, tron)


@bot.message_handler(commands = ['atom'])
def cosmos(message):
  atom = cg.get_price(ids='cosmos', vs_currencies='usd')
  cosmos = 'Cosmos   ' +'$ ' + str(atom['cosmos']['usd'])  
  bot.send_message(message.chat.id, cosmos)


@bot.message_handler(commands = ['near'])
def near(message):
  near = cg.get_price(ids='near', vs_currencies='usd')
  nearr = 'Near   ' +'$ ' + str(near['near']['usd'])  
  bot.send_message(message.chat.id, nearr)


@bot.message_handler(commands = ['link'])
def chainlink(message):
  link = cg.get_price(ids='chainlink', vs_currencies='usd')
  chainlink = 'Chainlink   ' +'$ ' + str(link['chainlink']['usd'])  
  bot.send_message(message.chat.id, chainlink)


@bot.message_handler(commands = ['avax'])
def avalanche(message):
  avax = cg.get_price(ids='avalanche-2', vs_currencies='usd')
  avalanche = 'Avalanche   ' +'$ ' + str(avax['avalanche-2']['usd'])  
  bot.send_message(message.chat.id, avalanche)


@bot.message_handler(commands = ['matic'])
def polygon(message):
  matic = cg.get_price(ids='matic-wormhole', vs_currencies='usd')
  polygon = 'Polygon   ' +'$ ' + str(matic['matic-wormhole']['usd'])  
  bot.send_message(message.chat.id, polygon)


@bot.message_handler(commands = ['xmr'])
def monero(message):
  xmr = cg.get_price(ids='monero', vs_currencies='usd')
  monero = 'Monero   ' +'$ ' + str(xmr['monero']['usd'])  
  bot.send_message(message.chat.id, monero)


@bot.message_handler(commands = ['ape'])
def apecoin(message):
  ape = cg.get_price(ids='apecoin', vs_currencies='usd')
  apecoin = 'ApeCoin   ' +'$ ' + str(ape['apecoin']['usd'])  
  bot.send_message(message.chat.id, apecoin)


@bot.message_handler(commands = ['sand'])
def sandbox(message):
  sand = cg.get_price(ids='the-sandbox', vs_currencies='usd')
  sandbox = 'Sandbox   ' +'$ ' + str(sand['the-sandbox']['usd'])  
  bot.send_message(message.chat.id, sandbox)


@bot.message_handler(commands = ['mana'])
def decentraland(message):
  mana = cg.get_price(ids='decentraland', vs_currencies='usd')
  decentraland = 'Mana   ' +'$ ' + str(mana['decentraland']['usd'])  
  bot.send_message(message.chat.id, decentraland)


@bot.message_handler(commands = ['axs'])
def axie(message):
  axs = cg.get_price(ids='axie-infinity', vs_currencies='usd')
  axie = 'Axs   ' +'$ ' + str(axs['axie-infinity']['usd'])  
  bot.send_message(message.chat.id, axie)


@bot.message_handler(commands = ['aave'])
def aave(message):
  aave = cg.get_price(ids='aave', vs_currencies='usd')
  aavee = 'Aave   ' +'$ ' + str(aave['aave']['usd'])  
  bot.send_message(message.chat.id, aavee)


@bot.message_handler(commands = ['lunc'])
def lunc(message):
  lunc = cg.get_price(ids='luna-wormhole', vs_currencies='usd')
  lunca = 'Lunc   ' +'$ ' + str(lunc['luna-wormhole']['usd'])  
  bot.send_message(message.chat.id, lunca)



bot.polling()
