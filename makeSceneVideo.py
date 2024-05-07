from datetime import datetime
from moviepy.editor import VideoClip, AudioFileClip, CompositeVideoClip, ImageClip, TextClip
from getWordTimestamps import getWordTimestamps

def create_caption_clip(word: str, start_time: float, end_time: float) -> VideoClip:
    # Create a TextClip for the word with specified start and end times
    text_clip = TextClip(word, font="Verdana-Bold", fontsize=24, color='white', bg_color="black")
    # Set the position of the text clip
    text_clip = text_clip.set_pos('center')
    # Set the start and end times of the text clip
    text_clip = text_clip.set_start(start_time).set_end(end_time)
    return text_clip

def makeSceneVideo(scene_number: int, audio_path: str, background_image_path: str, output_path: str, images: dict):
    
    # Parse the SRT file to get the words and their timings
    words_and_timings = getWordTimestamps(scene_number)
    
    # Initialize a list to hold the text clips
    clips = []
    
    # Initialize the current background image
    current_background_image = ImageClip(background_image_path)
    
    # Iterate over each word and its timestamp
    for start_time, end_time, word in words_and_timings:
        # Convert start_time and end_time from strings to datetime objects
        start_time_obj = datetime.strptime(start_time, "%H:%M:%S,%f")
        end_time_obj = datetime.strptime(end_time, "%H:%M:%S,%f")
        
        # Convert the start and end times to seconds
        clip_start_time = (start_time_obj - start_time_obj.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        clip_end_time = (end_time_obj - start_time_obj.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        
        # Create a text clip for the word
        text_clip = create_caption_clip(word, clip_start_time, clip_end_time)
        
        # Add the text clip to the list
        clips.append(text_clip)
    
    # Create a CompositeVideoClip with the current background image
    final_clip = CompositeVideoClip([current_background_image.set_duration(clips[-1].end)], size=current_background_image.size)
    
    # Overlay the text clips on the background image
    for clip in clips:
        final_clip = CompositeVideoClip([final_clip, clip.set_position(('center', 'center'))])
    
    # Add audio to the final clip
    audio_clip = AudioFileClip(audio_path)
    final_clip = final_clip.set_audio(audio_clip)
    
    # Write the final clip to a file
    final_clip.write_videofile(output_path, fps=24, codec='libx264')