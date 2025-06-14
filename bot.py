import os
import requests
from telegram import Bot
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN", "ใส่โทเคนบอทตรงนี้")
CHAT_ID = os.getenv("CHAT_ID", "ใส่ chat_id ตรงนี้")

def get_price():
    try:
        bitkub = requests.get("https://api.bitkub.com/api/market/ticker?sym=USDT_THB").json()
        cryptocompare = requests.get("https://min-api.cryptocompare.com/data/price?fsym=USDT&tsyms=THB").json()
        bk_price = bitkub["USDT_THB"]["last"]
        cc_price = cryptocompare["THB"]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"📢 แจ้งเตือนราคาคริปโต

เวลา: {now}
Bitkub: {bk_price:,.2f} บาท
CryptoCompare: {cc_price:,.2f} บาท"
        return msg
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    message = get_price()
    Bot(token=TOKEN).send_message(chat_id=CHAT_ID, text=message)
