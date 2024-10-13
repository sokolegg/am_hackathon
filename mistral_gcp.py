import requests

"""
MODEL="mistral-large"
MODEL_VERSION="2407"


url="https://europe-west4-aiplatform.googleapis.com/v1/projects/mistral-alan-hack24par-836/locations/europe-west4/publishers/mistralai/models/$MODEL@$MODEL_VERSION:rawPredict"


curl \
  -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  $url \
  --data '{
    "model": "'"$MODEL"'",
    "temperature": 0,
    "messages": [
      {"role": "user", "content": "What is the best French cheese?"}
    ]
}'
"""

url = "https://europe-west4-aiplatform.googleapis.com/v1/projects/mistral-alan-hack24par-836/locations/europe-west4/publishers/mistralai/models/mistral-large@2407:rawPredict"
token = "ya29.a0AcM612w4VpuTITeG2vmEwMKav0p4hSZ36eo4X_3iWjOnyMXln646rP7Lgk1KQ0U11x8UhfQRcz-UPz37C6rGNDnpYrf7bosw9uxcjeGkXS-0qsYc8o0xieaU6oFdJyndRPTKQk1DT7GMFIqJhHSBBnRgWad5UauiuyJd4-d0SHAMlwaCgYKAX0SARMSFQHGX2MiPmhGT-fsX84xk9NEoOqvZQ0181"

def process(prompt):
    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json={
                "model": "mistral-large",
                "temperature": 0,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()
        print(response.status_code)

        result = data["choices"][0]["message"]["content"]
        print(result)

        return result
    except Exception as e:
        print(e)
        return "Error"