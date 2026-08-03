import time
from function import scrape, extract, store, send_email, read


URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; '
                  'Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}
while True:
    scraped = scrape(URL)
    extracted = extract(scraped)
    message = f"Subject: Temperature update!\n\nAverage World Temperature Now: {extracted}"
    print(extracted)
    content = read(extracted)
    if extracted not in content:
        store(extracted)
        send_email(message.encode("utf-8"))
    time.sleep(2)