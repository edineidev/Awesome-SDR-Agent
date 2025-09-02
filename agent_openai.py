#from openai import OpenAI

def send(input_text: str):
    print(f"Send: {input_text}")

    #client = OpenAI()

    # response = client.responses.create(
    #     model="gpt-5-nano",
    #     input="Write a one-sentence bedtime story about a unicorn."
    # )
    response = { "output_text": "Hello World" }

    return response["output_text"]