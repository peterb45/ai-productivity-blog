from gpt4all import GPT4All

# Set the correct model path and force CPU usage
model_path = r"C:\Users\Owner\AppData\Local\nomic.ai\GPT4All\Llama-3.2-3B-Instruct-Q4_0.gguf"

# Load model with explicit CPU mode
gpt4all_model = GPT4All(model_path, allow_download=False)

def generate_article(topic):
    """Generates an AI-written blog post using GPT4All."""
    prompt = f"Write a 1,000-word SEO-optimized blog post about {topic}. Include an introduction, subheadings, and a conclusion."
    
    response = gpt4all_model.generate(prompt)
    return response

# List of topics for blog posts
topics = [
    "Best AI Productivity Tools in 2025",
    "How to Automate Your Business with AI",
    "10 AI Tools That Will Save You Hours Every Week"
]

# Generate articles for each topic
for topic in topics:
    article = generate_article(topic)
    filename = topic.replace(" ", "_") + ".md"  # Save as Markdown for GitHub Pages
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n{article}")
    print(f"✅ Article saved: {filename}")
