from time import sleep
from celery import shared_task
import requests


@shared_task
def notify_customers(message):
    # Logic to send notifications to customers
    print("sending 10k emails")
    print(message)
    sleep(10)
    print("emails sent")


# @shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True)
# def fetch_news(self):
#     print("Trying to fetch news...")
#     response = requests.get("https://some-news-api.com/data")

#     print("Status Code:", response.status_code)
#     print("Response Text:", response.text[:500])  # print first 500 characters

#     try:
#         data = response.json()
#         print("Parsed JSON:", data)
#     except Exception as e:
#         print("JSON Decode Error:", str(e))
#         raise e  # Let Celery retry it


# @shared_task
# def send_email_batch(emails):
#     for email in emails:
#         print(f"Sending email to {email}")
#     print("Batch complete.")
