from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def makeFinalVideo():
    video_dir = 'assets/temp/video'
    all_files = os.listdir(video_dir)
    scene_files = [f for f in all_files if f.startswith('scene_') and f.endswith('.mp4')]

    # Sort the scene files based on the scene number extracted from the file name
    scene_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

    video_clips = []
    for scene_file in scene_files:
        clip = VideoFileClip(os.path.join(video_dir, scene_file))
        video_clips.append(clip)

    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile('./assets/temp/video/final_video.mp4', codec='libx264')