from dotenv import load_dotenv

import agent_openai as openai

load_dotenv()

if __name__ == '__main__':
    print(f"Recived: {openai.send("Hi")}")
