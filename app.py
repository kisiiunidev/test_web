import os
from pathlib import Path

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


@app.route("/api/paths")
def paths():

    paths = []

    for root in [
        "/var/task",
        "/var/task/_vendor",
        "/tmp",
        "/home"
    ]:
        if os.path.exists(root):
            paths.append({
                "path": root,
                "contents": os.listdir(root)[:100]
            })

    return jsonify({
        "playwright_browsers_path": os.environ.get(
            "PLAYWRIGHT_BROWSERS_PATH"
        ),
        "playwright_cache": str(
            Path.home() / ".cache" / "ms-playwright"
        ),
        "paths": paths
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