from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Server Running"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)

        message = data.get("message", "").strip()
        image = data.get("image")

        msg = message.lower()

        # 🔥 Smart intent detection
        image_words = ["image", "img", "photo", "picture", "screenshot"]
        intent_words = ["describe", "explain", "analyze", "what is in", "what's in"]

        # 🚫 Block ONLY when user wants to analyze an image but didn't upload
        if not image:
            if any(i in msg for i in intent_words) and any(w in msg for w in image_words):

                # ✅ Allow normal language questions
                safe_words = ["word", "meaning", "define"]
                if not any(s in msg for s in safe_words):
                    return jsonify({"reply": "⚠️ Please upload an image first."})

        # 🔧 Build request
        payload = {
            "model": "llava",
            "prompt": message if message else "Describe this image clearly",
            "stream": False
        }

        # 🖼️ Handle image safely
        if image:
            if "," in image:
                image = image.split(",")[1]  # remove base64 header
            payload["images"] = [image]

        # 🚀 Call Ollama
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json=payload,
            timeout=60
        )

        # ⚠️ Handle API errors
        if response.status_code != 200:
            return jsonify({"reply": "❌ Ollama Error: " + response.text})

        result = response.json()
        reply = result.get("response", "No response from AI")

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"reply": "❌ Server Error: " + str(e)})

if __name__ == "__main__":
    print("✅ SERVER STARTED")
    app.run(port=5050, debug=True)