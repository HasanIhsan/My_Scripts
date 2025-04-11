import json
import random

topics = {
    "Science": ["black holes", "quantum physics", "neuroscience"],
    "Technology": ["AI ethics", "web development", "cybersecurity"],
    "Philosophy": ["existentialism", "ethics", "consciousness"],
    "Cooking": ["baking techniques", "international cuisines", "meal prep"],
    "Self-Improvement": ["productivity", "mindfulness", "career growth"]
}

conversations = []

# Generate 100 base entries
for _ in range(100):
    category = random.choice(list(topics.keys()))
    subtopic = random.choice(topics[category])
    
    entry = {
        "user": f"Tell me about {subtopic} in {category}",
        "bot": f"Detailed explanation of {subtopic} including key concepts, historical context, and modern applications in the field of {category}..."
    }
    conversations.append(entry)

# Add follow-up conversations
for _ in range(50):
    previous = random.choice(conversations)
    entry = {
        "user": f"Going deeper into {previous['user'].split()[-1]}",
        "bot": f"Advanced discussion expanding on previous topic, including technical details and case studies..."
    }
    conversations.append(entry)

# Save to file
with open("expanded_memory.json", "w") as f:
    json.dump({"conversation_history": conversations}, f, indent=2)