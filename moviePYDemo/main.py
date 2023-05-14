import numpy as np
from moviepy.editor import *

video_clip = VideoFileClip("video.mp4")

image_clip = ImageClip("image.png").set_duration(video_clip.duration)


def simple_motion(t):
    # 1920
    # 1080
    return t*5, t*5


image_clip = image_clip.set_position(simple_motion)

final_clip = CompositeVideoClip([video_clip, image_clip])

final_clip.write_videofile("output-simple.mp4", fps=video_clip.fps)
