import subprocess

def ai_writer(prompt, model="llama3"):
    """
    Uses a local Ollama model (default: LLaMA3) to generate text based on the prompt.
    """
    command = ['ollama', 'run', model]
    print("✍️  AI Writer is generating content...")
    try:
        result = subprocess.run(command, input=prompt.encode(), capture_output=True)
        output = result.stdout.decode()
        return output.strip()
    except Exception as e:
        print("❌ AI Writer Error:", e)
        return "Failed to generate content."

def ai_reviewer(text, model="llama3"):
    """
    Uses the same or different model to review and refine the AI-generated content.
    """
    review_prompt = f"Please improve and polish the following chapter for grammar, coherence, and style:\n\n{text}"
    return ai_writer(review_prompt, model=model)
