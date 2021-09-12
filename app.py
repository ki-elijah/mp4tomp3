import moviepy.editor as mp
video = mp.VideoFileClip(r"jammcard.mp4")
video.audio.write_audiofile(r"audio.mp3")
