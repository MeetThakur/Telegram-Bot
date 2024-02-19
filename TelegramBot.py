import telebot
import requests 
from bs4 import BeautifulSoup as b
import random as r

gptkey = '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'

def randomPickupLine():
    req = requests.get('https://www.generatormix.com/random-pick-up-lines?number=1')
    soup = b(req.text,'html.parser')
    result = soup.find("blockquote",class_="text-left").text
    return result

def randomMotivation():
    req = requests.get('https://www.generatormix.com/random-inspirational-quotes?number=1')
    soup = b(req.text,'html.parser')
    result = soup.find("blockquote",class_="text-left").text
    return result

def randomQuote():
    req = requests.get('https://www.generatormix.com/random-love-quotes?number=1')
    soup = b(req.text,'html.parser')
    result = soup.find("blockquote",class_="text-left").text
    return result

def randomAnswer():
    req = requests.get('https://www.generatormix.com/random-answer-generator?number=1')
    soup = b(req.text,'html.parser')
    result = soup.find("h2",class_="text-center").text
    return result

def randomQuestion():
    req = requests.get('https://www.generatormix.com/random-things-to-ask-a-girl?number=1')
    soup = b(req.text,'html.parser')
    result = soup.find("blockquote",class_="text-left").text
    return result


def randomFact():
    global text
    req = r.randint(1,4)
    if req == 1:        
        req = requests.get("https://www.generatormix.com/random-facts-generator?number=1")
    elif req == 2:
        req = requests.get("https://www.generatormix.com/random-animal-facts?number=1")
    elif req == 3:
        req = requests.get("https://www.generatormix.com/random-science-facts?number=1")
    elif req == 4:
        req = requests.get("https://www.generatormix.com/random-weird-facts?number=1")

    soup = b(req.text,"html.parser")
    s = soup.find("blockquote")
    fact = s.text
    return fact

def findmeaning(text):
    req1 = requests.get("https://www.google.com/search?q=define+"+text)
    soup1 = b(req1.text,"html.parser")
    s = soup1.find("div",class_="Gx5Zad xpd EtOod pkphOe")
    result = s.text
    if result.startswith("Name"):
        temp = result.split(":")
        temp2 = temp[2].split(".")
        return temp2[0]
    elif result.startswith("Did you mean"):
        temp = result.split(":")
        t = temp[1]
        result = findmeaning(t[8:])
        return result
    elif result.startswith("Showing results for") or result.startswith("People also ask") or "askWhat" in result:
        return "Sorry, Meaning Not Found"
    else:
        rl = result.split(".")
        result = rl[0]
        return result


token = "6089514862:AAGu9KoN-1QDYjnGwRT5DgvN0V-UpCe9Chw"
bot = telebot.TeleBot(token)

@bot.message_handler(["help"])
def help(msg):
    bot.reply_to(msg,"List Of Commands\n1: Tell me a Fact\n2: Tell me a Pickup Line\n3: Tell me a quote\n4: Motivate me\n5: Ask me a question")

@bot.message_handler(["fact"])
def start(msg):
    bot.reply_to(msg,randomFact())

@bot.message_handler(["quote"])
def start(msg):
    bot.reply_to(msg,randomQuote())

@bot.message_handler(["motivate"])
def start(msg):
    bot.reply_to(msg,randomMotivation())

@bot.message_handler(["question"])
def start(msg):
    bot.reply_to(msg,randomQuestion())

@bot.message_handler(["pickup"])
def start(msg):
    bot.reply_to(msg,randomPickupLine())

    
    

@bot.message_handler()
def mean(msg):
    if msg.text.lower() == "nitya" or  msg.text.lower() == "/nitya":
        bot.reply_to(msg,findmeaning(msg.text)+"\nand aslo a PAGAL AURAT")
    elif msg.text.lower().startswith('tell me a fact') or msg.text.lower() == 'fact':
        bot.reply_to(msg,randomFact())

    elif msg.text.lower().startswith('tell me a pickup line'):
        bot.reply_to(msg,randomPickupLine())

    elif msg.text.lower().startswith('motivate me'):
        bot.reply_to(msg,randomMotivation())

    elif msg.text.lower().startswith('ask me a question'):
        bot.reply_to(msg,randomQuestion())

    elif msg.text.lower().startswith('tell me a quote'):
        bot.reply_to(msg,randomQuote())        
    else:
        if msg.text.lower().endswith("?"):
            bot.reply_to(msg,randomAnswer())
        else:
            bot.reply_to(msg,findmeaning(msg.text))
            

bot.polling()





