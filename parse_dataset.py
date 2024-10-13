import json
import glob
import os

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data['questions']:
                yield {
                    "role": "user",
                    "content": item['question']
                }, {
                    "role": "assistant",
                    "content": item['right_answers']
                }
    except json.JSONDecodeError as e:
        print(f"Error parsing {file_path}: {e}")
    except KeyError as e:
        print(f"Missing expected key in {file_path}: {e}")
    except Exception as e:
        print(f"Unexpected error processing {file_path}: {e}")

def main():
    train_output_file = 'data/dataset.jsonl'
    eval_output_file = 'data/eval_dataset.jsonl'
    input_files = glob.glob('data/jsons/*.json')  # Adjust the pattern if your files have a specific naming convention

    all_messages = []

    for file_path in input_files:
        print(f"Processing {file_path}...")
        all_messages.extend(list(process_file(file_path)))

    output_data = [{"messages": message} for message in all_messages]

    train_data = output_data[:int(len(output_data)*0.8)]
    eval_data = output_data[int(len(output_data)*0.8):]

    with open(train_output_file, 'w') as outfile:
        for message in train_data:
            s = json.dumps(message)
            outfile.write(s + '\n')

    with open(eval_output_file, 'w') as outfile:
        for message in eval_data:
            s = json.dumps(message)
            outfile.write(s + '\n')

    print(f"Conversion complete. Output saved to {train_output_file}")

if __name__ == "__main__":
    main()