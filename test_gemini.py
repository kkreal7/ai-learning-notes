from google import genai

# パソコンの一時記憶（環境変数 GEMINI_API_KEY）から自動で安全にキーを読み込みます
client = genai.Client()

# 最新のモデルを指定してGeminiに送信！
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="こんにちは！自己紹介を1行でしてください。"
)

# AIからの返事を画面に表示
print("\n--- Geminiからの返事 ---")
print(response.text)