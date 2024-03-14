from openai import OpenAI

client = OpenAI()

# Create a request to obtain embeddings
response = client.embeddings.create(
    model = "text-embedding-ada-002", 
    input = "Who is Cinderella!"
)

# Convert the response into a dictionary
response_dict = response.model_dump()

print(response_dict)