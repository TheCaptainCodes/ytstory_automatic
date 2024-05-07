import requests

def textToMp3(text, scene_number):
    url = "https://natural-text-to-speech-converter-at-lowest-price.p.rapidapi.com/backend/ttsNewDemo"

    payload = {
        "ttsService": "polly",
        "audioKey": "ff63037e-6994-4c50-9861-3e162ee56468",
        "storageService": "s3",
        "text": text,
        "voice": {
            "value": "en-US_Matthew",
            "lang": "en-US"
        },
        "audioOutput": {
            "fileFormat": "mp3",
            "sampleRate": 24000
        }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "07a698f8bbmsh53998e8e53aa58ap1d614fjsndd810c45e847",
        "X-RapidAPI-Host": "natural-text-to-speech-converter-at-lowest-price.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    # Check if the request was successful
    if response_json['success']:
        # Get the URL of the audio file
        audio_url = response_json['url']
        # Make a GET request to the audio URL
        audio_response = requests.get(audio_url)
        # Define the path where you want to save the audio file
        save_path = f'assets/temp/mp3/scene_{scene_number}_audio.mp3'
        # Write the content of the response to a file
        with open(save_path, 'wb') as audio_file:
            audio_file.write(audio_response.content)
        return save_path
    else:
        print(f"Failed to generate audio for scene {scene_number}.")