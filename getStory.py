import requests
import json

def getStory(personal_access_token, bot_id, query):

    # API endpoint
    url = f"https://api.coze.com/open_api/v2/chat"

    # Request headers
    headers = {
        "Authorization": f"Bearer {personal_access_token}",
        "Content-Type": "application/json"
    }

    # Request body
    body = {
        "query": query,
        "bot_id": bot_id,
        "user": personal_access_token
    }

    # Sending POST request to Coze API
    response = requests.post(url, headers=headers, json=body)

    # Check if request was successful
    if response.status_code == 200:
        # Convert the response content to a Python dictionary
        response_data = response.json()
        print(response_data)
        
        # Initialize a dictionary to store the story values
        story_values = {}
        
        # Now you can access 'messages' and other keys
        for message in response_data['messages']:
            if 'content' in message:
                try:
                    # Parse the JSON content
                    content = json.loads(message['content'])

                    # Check if 'youtube_title' is in the content
                    if 'youtube_video_title' in content:
                        # Extract the desired fields and store them in the dictionary
                        story_values['title'] = content.get('youtube_video_title', '')
                        story_values['description'] = content.get('youtube_video_description', '')
                        story_values['story'] = content.get('story', [])
                        story_values['keywords'] = content.get('keywords', [])
                        
                        # Stop after finding the first match
                        break

                except json.JSONDecodeError:
                    # print("Error parsing JSON content:", message['content'])
                    continue
    else:
        print("Error:", response.text)

    # Now you can use the story_values dictionary as needed
    return story_values