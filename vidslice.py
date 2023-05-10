from moviepy import editor
import math
import random

# TODO pass as args
filename = "/home/lain/bakudan-dec17-2022.mp4"
bpm = 220
slice_beats = 1./1.
output_seconds = 5.

slice_seconds = lambda bpm, slice_beats: (60/bpm) * slice_beats


clip = editor.VideoFileClip(filename)
slice_duration = slice_seconds(bpm, slice_beats)
output_slices = output_seconds / slice_duration

print("output slices: ", output_slices)

slices = []

for i in range(math.ceil(output_slices)):
    slice_start = random.randint(0, math.floor(clip.duration-slice_duration))
    slice_end = slice_start + slice_duration
    slices.append(clip.subclip(slice_start, slice_end))

output = editor.concatenate_videoclips(slices)
output.write_videofile("/home/lain/videoslicetest.mp4")

