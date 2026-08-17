import os
import time

print("Database Username:", os.getenv("DB_USERNAME"))
print("Database Password:", os.getenv("DB_PASSWORD"))

while True:
    time.sleep(60)
