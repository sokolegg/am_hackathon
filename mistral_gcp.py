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
token = "ya29.a0AcM612xie74ijLBAYYswyiH8w3qVZrQsK0sJ2-1WCJziz5U_3rWyQnXgQYfyTOe_hTnkN0zEVKoTiZgNxIXAvofrIzA4m1BCl4gneM0GOQhcjd-U68THV7yl4kRZGNSYC_zScBEsQbTsR_uSYKaXjfTEnm2S0yX_ucBs1tyJjkW4AAaCgYKAR0SARMSFQHGX2MiMo9d1lSXM_win--zLOEhDA0181"

def process(prompt):
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

    result = data["choices"][0]["message"]["content"]
    print(result)

    return result