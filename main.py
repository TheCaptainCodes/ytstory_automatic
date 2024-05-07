import os
from makeSceneVideo import makeSceneVideo
from getStory import getStory
from generateImages import generateImages
from textToMp3 import textToMp3
from makeFinalVideo import makeFinalVideo

# Coze AI
personal_access_token = "pat_TzCEzjWUqIU95bOQTJrCjvFvq7EHxRJ0K48Ipvkbb8iuqp6Q9QJoTs39R1CoY0n0"
bot_id = "7365106000677830661"
query = """
a very short detective mystery to solve. Give clues and suspects. And at the end ask the solution to the viewers.
"""

# Stability AI
engine_id = "stable-diffusion-v1-6"
api_host = "https://api.stability.ai"
api_key = "sk-5UR7pqpFQ1wuco4n7gEL6JIZynrlBUJoQT6nKoXV1L5qUYZp"

if __name__ == "__main__":
    story_values = getStory(personal_access_token, bot_id, query)
    # print(story_values, "\n")

    images = generateImages(story_values["keywords"], engine_id, api_host, api_key)
    print("Images generated..")
    print("Scene Generation starting..\n")

    for scene in story_values["story"]:
        scene_number = scene["scene"]
        plain_text = scene["plain_text"]
        tts_text = scene["tts_text"]
        background_image_path = images[scene_number]

        audio_filepath = textToMp3(tts_text, scene_number)
        print(f"Scene {scene_number} MP3 Generated..")

        scene_video_output = f"./assets/temp/video/scene_{scene_number}.mp4"
        makeSceneVideo(scene_number, audio_filepath, background_image_path, scene_video_output, images)
        print(f"Scene {scene_number} video Generated..")
    
    makeFinalVideo()
