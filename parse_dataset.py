import os
import json

def parse_json_files(input_dir, output_file_path):
    # Initialize a list to hold the output data
    output_data = []

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            # Construct the full file path
            file_path = os.path.join(input_dir, filename)

            # Read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)

                # Process each question in the input data
                for question_data in data['questions']:
                    question = question_data['question']
                    right_answer = question_data['right_answers']

                    # Create the user and assistant messages
                    user_message = {
                        "role": "user",
                        "content": question
                    }
                    assistant_message = {
                        "role": "assistant",
                        "content": right_answer
                    }

                    # Create the message list for this question
                    messages = [
                        user_message,
                        assistant_message
                    ]

                    # Add the message list to the output data
                    output_data.append({
                        "messages": messages
                    })

    # Write the output data to the output JSON file
    with open(output_file_path, 'w') as output_file:
        json.dump(output_data, output_file, indent=4)

    print(f"Data has been written to {output_file_path}")

if __name__ == "__main__":
    # Define the input and output directories and file paths
    input_dir = 'input_dir'
    output_file_path = 'output_dir/your_output_file.json'

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Call the parser function
    parse_json_files(input_dir, output_file_path)
