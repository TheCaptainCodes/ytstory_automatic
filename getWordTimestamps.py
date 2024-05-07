import stable_whisper
import re

def getWordTimestamps(scene_number):
    srt_path = f"./assets/temp/srt/scene_{scene_number}_srt.srt"
    
    model = stable_whisper.load_model('base')
    result = model.transcribe(f'./assets/temp/mp3/scene_{scene_number}_audio.mp3')
    result.to_srt_vtt(srt_path)

    timestamps_and_phrases = {}
    with open(srt_path, 'r', encoding='utf-8-sig') as file:
        srt_content = file.read()

    # Define regular expression pattern to match timestamps and phrases
    pattern = r'(\d+)\s*(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\s*(.*?)(?=\n|$)'
    matches = re.findall(pattern, srt_content, re.DOTALL)

    for match in matches:
        # Extract start and end times
        start_time = match[1]
        end_time = match[2]

        # Extract and clean the phrase
        phrase = match[3]
        phrase = re.sub(r'<font color="#.*?">', '', phrase)  # Replace with empty string
        phrase = re.sub(r'</font>', '', phrase)  # Remove closing tag

        # Check if the phrase already exists in the dictionary
        if phrase in timestamps_and_phrases:
            # If the phrase exists, update only the end time
            current_start_time, _ = timestamps_and_phrases[phrase]
            timestamps_and_phrases[phrase] = (current_start_time, end_time)
        else:
            # If the phrase is new, add it to the dictionary
            timestamps_and_phrases[phrase] = (start_time, end_time)

    # Convert the dictionary to a list of tuples
    return [(start_time, end_time, phrase) for phrase, (start_time, end_time) in timestamps_and_phrases.items()]