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

