from nemoguardrails.rails import LLMRails, RailsConfig

def main():
    config = RailsConfig.from_path("./config")
    rails = LLMRails(config)

    response = rails.generate(messages=[{
        "role": "user",
        "content": "What can you do for me?"
    }])
    print(response)

if __name__ == "__main__":
    main()
