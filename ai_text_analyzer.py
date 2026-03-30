# ai_text_analyzer.py

def analyze_text(text):
    # Simple "AI-like" logic (demo version)
    
    # Summary: first 2 sentences or first 120 chars
    sentences = text.split(".")
    summary = ".".join(sentences[:2]).strip()
    
    if len(summary) < 20:
        summary = text[:120] + "..." if len(text) > 120 else text

    # Fake key points extraction
    words = text.split()
    keywords = list(set(words[:5]))

    key_points = "\n".join([f"- {word}" for word in keywords])

    return f"📌 Summary:\n{summary}\n\n🔑 Key Points:\n{key_points}"


if __name__ == "__main__":
    print("🔍 AI Text Analyzer (No API Version)")
    
    user_input = input("\nEnter text:\n\n")
    
    result = analyze_text(user_input)
    
    print("\n🧠 Result:\n")
    print(result)