import os
from pytubefix import YouTube

def download_audio_from_youtube(url: str, destination: str = "./downloads") -> str:

    # Ensure the destination directory exists
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Initialize the YouTube object
    yt = YouTube(url)

    # Extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # Download the file
    out_file = video.download(output_path=destination)

    # Save the file as .mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # Print success message
    print(f"{yt.title} has been successfully downloaded to {new_file}.")

    return new_file

# Example usage
if __name__ == "__main__":
    # Replace these variables with your desired values
    youtube_url = "https://www.youtube.com/watch?v=VWqxvBQKwKQ"  # Replace with your YouTube video URL
    save_path = r"C:\Users\82107\OneDrive\바탕 화면\해커톤"  # Replace with your desired save path

    download_audio_from_youtube(youtube_url, save_path)