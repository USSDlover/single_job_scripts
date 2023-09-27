import re
import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip


def parse_srt(srt_path):
    with open(srt_path, 'r') as f:
        lines = f.read()

    sub_pieces = re.findall(r'(\d+)\n([\d:,]+) --> ([\d:,]+)\n(.+?)(?=\n\d|\Z)', lines, re.DOTALL)
    return sub_pieces


def split_video_by_subs(video_path, subs):
    video_clip = VideoFileClip(video_path)

    for idx, (sub_idx, start_time, end_time, text) in enumerate(subs, start=1):
        start_seconds = time_to_seconds(start_time)
        end_seconds = time_to_seconds(end_time)

        sub_video = video_clip.subclip(start_seconds, end_seconds)
        sub_video_path = f"sub_video_{idx}.mp4"
        sub_video.write_videofile(sub_video_path, codec='libx264')

        sub_srt = f"{sub_idx}\n{start_time} --> {end_time}\n{text}\n"
        sub_srt_path = f"sub_srt_{idx}.srt"
        with open(sub_srt_path, 'w') as f:
            f.write(sub_srt)


def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


if __name__ == "__main__":
    main_video_path = "input_video.mp4"
    main_srt_path = "input_subtitle.srt"

    parsed_subs = parse_srt(main_srt_path)
    split_video_by_subs(main_video_path, parsed_subs)
