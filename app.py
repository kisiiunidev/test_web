import os

os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "service": "Flask + Playwright",
        "message": "API is running"
    })


@app.route("/api/test")
def test_playwright():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            "https://example.com",
            wait_until="domcontentloaded"
        )

        title = page.title()
        url = page.url

        browser.close()

    return jsonify({
        "success": True,
        "title": title,
        "url": url
    })