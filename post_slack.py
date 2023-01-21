from slack_sdk import WebClient
from selenium import webdriver
import time
import json

#webdriverのパス
driver=webdriver.Chrome("C:\python\chromedriver.exe")
#アクセス
driver.get("https://google.co.jp")
# 何かスクレイピング
time.sleep(3)
#webdriverを閉じる
driver.quit()

# トークンjsonファイルの読み込み
with open("./env/slack_token.json", "r") as json_file:
		info = json.load(json_file)

SLACK_ACCESS_TOKEN = info['token']
CHANNEL_ID = '#test'

# Slackクライアントを作成
client = WebClient(SLACK_ACCESS_TOKEN)

# パブリックチャンネルにメッセージを投稿（chat.postMessageメソッド）
msg = "メッセージ"
response = client.chat_postMessage(channel=CHANNEL_ID, text=msg, icon_emoji=':robot_face:', username='スクレイピングBot')
