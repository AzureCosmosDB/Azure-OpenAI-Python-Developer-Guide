pip install -r requirements.txt

uvicorn app:app --host "0.0.0.0" --port 4242 --forwarded-allow-ips "*" --proxy-headers

