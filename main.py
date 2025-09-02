from dotenv import load_dotenv
#from openai import OpenAI

load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #client = OpenAI()

    # response = client.responses.create(
    #     model="gpt-5-nano",
    #     input="Write a one-sentence bedtime story about a unicorn."
    # )
    response = { "output_text": "Hello World" }

    print(response["output_text"])
