import ollama
import os


model = "llama3.2:1b"

#you can add your file location
input_file = "your location"
output_file = "your location"


# Check if input file exists
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' does not exist.")
    exit(1)
   


with open(input_file, 'r') as f:
    items = f.read().strip()
   
   

prompt = f"""


Here is your list:

{items}

Please:

1.categorize them into dairy and vegtables and foods
2.write down benefits of each one of them 

"""
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", " ")  

    
    with open(output_file, 'w') as f:
        f.write(generated_text.strip())

    print(f"Categorized list has been saved to '{output_file}'.")
    #print (f" this is your list : {generated_text}")
except Exception as e:
    print("An error happens:", str(e))
