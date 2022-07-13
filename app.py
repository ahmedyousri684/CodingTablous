from flask import Flask, request, Response

app = Flask(__name__)

VERIFY_TOKEN = 'woodyfordecorations2022'
PAGE_ACCESS_TOKEN = 'EAAF9FZCRQ3iEBANR1SyMFYSZAOWvNKtERYDRCbbTdYQiYnYFNIniehFA0fnCA2LbKhXeJsooxj3IwZBaZA0pSfHa3sNsEMR4JUOZARkS7T5a3NZBaUxkkASSO5kt1H9AX2ChCHQBfTqBaBcmHy82NjJ1EkUcTwXZAXm6JUZB3dcNInkn6zJfcpqHI1djmsVeqwcZD'

@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"


app.run()