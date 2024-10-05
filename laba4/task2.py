from moviepy.editor import *
from PIL import Image
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('movie')
parser.add_argument('start')
parser.add_argument('finish')
parser.add_argument('frames')
parser.add_argument('-step', default=10)
clip = VideoFileClip(parser.parse_args().movie)
clip = clip.subclip(parser.parse_args().start, parser.parse_args().finish)
frames = int(clip.fps * clip.duration)
for i in range(0, frames, int(parser.parse_args().step)):
    frame = clip.get_frame(i*(clip.duration/frames))
    image = Image.fromarray(frame)
    image_new = image.resize((250,250))
    image_new.save(parser.parse_args().frames+f'/{i}.jpg')