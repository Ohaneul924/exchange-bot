# exchange_bot.py
import requests

import os

TOKEN = os.getenv('7627124447:AAENNOL8sZv8Gs85MTReLDCMxxoIKwLEk7M')
CHAT_ID = os.getenv('7697525666')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

def get_exchange_rate():
    url = "https://api.exchangerate.host/latest?base=USD"
    response = requests.get(url)
    data = response.json()

    rates = data.get('rates', {})
    krw = rates.get('KRW')
    jpy = rates.get('JPY')
    cny = rates.get('CNY')

    if krw and jpy and cny:
        message = (
            "📢 환율 정보 (USD 기준)\n"
            f"🇰🇷 KRW: {krw:.2f}\n"
            f"🇯🇵 JPY: {jpy:.2f}\n"
            f"🇨🇳 CNY: {cny:.2f}"
        )
        print("✔️ 메시지 전송됨:", message)
        send_telegram_message(message)
    else:
        print("❌ 환율 데이터를 가져올 수 없습니다.")

if __name__ == "__main__":
    get_exchange_rate()
