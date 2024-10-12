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
token = "ya29.a0AcM612xrC3KWzOqLUiE8o-hyapvidZzvyfQgMW6Yuj9F1BXyrlUpT7IHr91YEniRs-plezUlGWOcFLbWSFT8-hRVJGCx1z_R4MtHKQWCWGxMM4FXBnbFPA5juZVJR2pNRmmvSAk3b8FTzsfLSckQdlkCFivwrQR4HjNR984KYHtdxQaCgYKAZMSARMSFQHGX2Mijg-TxmW184dDgmggioGi6Q0181"

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