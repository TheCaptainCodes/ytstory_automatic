import requests

url = "https://natural-text-to-speech-converter-at-lowest-price.p.rapidapi.com/backend/ttsNewDemo"

payload = {
	"ttsService": "polly",
	"audioKey": "ff63037e-6994-4c50-9861-3e162ee56468",
	"storageService": "s3",
	"text": "<speak><p>Detective Reed stepped into the moonlit room, <break time='0.5s'/> eyes scanning for clues. The safe was open, <break time='0.5s'/> the pearls gone. Only a feather, <break time='0.5s'/> a glove, <break time='0.5s'/> and a ticket stub lay on the ground. 'The thief is someone at tonight's opera,' she mused aloud. <break time='1s'/> 'Who do you think took them?' she asked the viewers, pointing to the evidence.</p></speak>",
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

print(response.json())