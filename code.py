import os
import requests

# Define your API key and Database ID
API_KEY = 'ntn_A4774615209aFsUbtglDZxrwOAbyAcHm16ZRs3u48BHg6V'  # replace with your Notion API key
DATABASE_ID = '14711c96d8a98123a925000c3107e8c6'  # replace with your database ID

# Set the Notion API endpoint
url = f'https://api.notion.com/v1/pages'

# Define the headers for the request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2024-06-28"  # Use the latest version of the Notion API
}

# Define the data you want to send (task details)
data = {
    "parent": {"database_id": DATABASE_ID},
    "properties": {
        "Name": {"title": [{"text": {"content": "Complete Python Project"}}]},
        "Status": {"select": {"name": "In Progress"}},
        "Due Date": {"date": {"start": "2024-11-25"}}
    }
}

# Send the POST request to create a new task
response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
# Check the response from the API
if response.status_code == 200:
    print("Task added successfully!")
else:
    print(f"Failed to add task. Status code: {response.status_code}")
    print("Error response:", response.json())
