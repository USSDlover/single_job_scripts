import re
import subprocess


def parse_srt(srt_path):
    with open(srt_path, 'r') as f:
        lines = f.read()

    subs = re.findall(r'(\d+)\n([\d:,]+) --> ([\d:,]+)\n(.+?)(?=\n\d|\Z)', lines, re.DOTALL)
    return subs


def split_video_by_subs(video_path, subs):
    for idx, (sub_idx, start_time, end_time, text) in enumerate(subs, start=1):
        sub_video_path = f"sub_video_{idx}.mkv"
        sub_srt = f"{sub_idx}\n{start_time} --> {end_time}\n{text}\n"
        sub_srt_path = f"sub_srt_{idx}.srt"

        # Use ffmpeg to extract the portion of the video
        ffmpeg_command = [
            "ffmpeg",
            "-i", video_path,
            "-ss", start_time,
            "-to", end_time,
            "-c:v", "copy",
            "-c:a", "copy",
            sub_video_path
        ]
        subprocess.run(ffmpeg_command)

        # Write the SRT content to the SRT file
        with open(sub_srt_path, 'w') as f:
            f.write(sub_srt)


if __name__ == "__main__":
    main_video_path = "input_video.mkv"
    main_srt_path = "input_subtitle.srt"

    parsed_subs = parse_srt(main_srt_path)
    split_video_by_subs(main_video_path, parsed_subs)
