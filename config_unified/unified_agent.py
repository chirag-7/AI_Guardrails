import os
from nemoguardrails import LLMRails, RailsConfig

# 1. Define the Custom Actions (Tools) for Layer 3
async def get_weather(location):
    # In a real app, this would call a weather API
    return f"The weather in {location} is sunny and 25°C."

async def check_facts(context, response):
    # Simple mock for Layer 4: Check if the bot mentioned "aliens" (hallucination)
    if "aliens" in response.lower():
        return 0.0  # Low accuracy score
    return 1.0  # High accuracy score

# 2. Load the Unified Configuration
config = RailsConfig.from_path("./config_unified")
app = LLMRails(config)

# 3. Register the Actions
app.register_action(get_weather, "get_weather")
app.register_action(check_facts, "check_facts")

# 4. Run the Agent
def main():
    print("🛡️  Unified Guardrails Agent (All 4 Layers Active) 🛡️")
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["quit", "exit"]:
            break
            
        try:
            response = app.generate(messages=[{
                "role": "user",
                "content": user_input
            }])
            print(f"Bot: {response['content']}")
        except Exception as e:
            print(f"🛑 Blocked by Guardrails: {e}")

if __name__ == "__main__":
    main()
