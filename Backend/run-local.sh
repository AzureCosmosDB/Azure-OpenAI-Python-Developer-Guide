pip install -r requirements.txt

uvicorn app:app --host "0.0.0.0" --port 80 --forwarded-allow-ips "*" --proxy-headers

