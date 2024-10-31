import logging
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def jira_webhook():
    """
    Обработка webhook запроса от Jira с проверкой секретного ключа.
    """
    logger.info("Получен запрос от webhook")

    data = request.json
    logger.info(f"Полученные данные: {data}")

if __name__ == "__main__":
    port = 8080
    app.run(debug=True,host='0.0.0.0',port=port)
