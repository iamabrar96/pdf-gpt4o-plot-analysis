import base64
import openai 
import os

# Set the OpenAI API key
openai.api_key = "******************"
# Open the image file and encode it as a base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# your image path 
image_path = '' 
base64_image = encode_image(image_path)
MODEL = "gpt-4o"


# Create a chat completion
response = openai.ChatCompletion.create(
    model="gpt-4o",  # Use the appropriate model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds the output as CSV format"},
        {"role": "user", "content": [
            {"type": "text", "text": "The given image is a graph plot which consists of x -axis and y-axis.The shape recovery ratio as a function of aging temperature for the Fe-30Mn-6Si-5Cr-Re alloys.(a) no Re-addition, (b) 0.05 Re,(c) 0.1 Re, (d) 0.3 Re .Please do not write any additional text just headers , columns and rows must be included in the csv file.can you understand the given image and explain it's detail in a CSV format?"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ],
    temperature=0.0,
)

# Extract the assistant's response
assistant_response = response.choices[0].message['content']

# Print the response (optional)
print("Assistant:", assistant_response)

# Save the response to a text file
output_file_path = "s11665-014-1071-z_image_output.csv"
with open(output_file_path, "w") as file:
    file.write(assistant_response)

print(f"Response saved to {output_file_path}")
