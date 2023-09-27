from moviepy.editor import VideoFileClip


def convert_mkv_to_mp4(input_file, output_file):
    try:
        # Load the MKV video clip
        video_clip = VideoFileClip(input_file)

        # Generate the MP4 output file
        video_clip.write_videofile(output_file, codec='libx264')

        print(f"Conversion successful: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")


if __name__ == "__main__":
    input_file = "input_video.mkv"  # Replace with the path to your input MKV video
    output_file = "output_video.mp4"  # Replace with the desired output MP4 file name

    convert_mkv_to_mp4(input_file, output_file)
