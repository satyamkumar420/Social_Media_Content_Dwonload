# Social Media Content Downloader
import instaloader as il
import os
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import urllib.parse



# --------------------------------------------------------
#  1. Install Library instaloader and pytube
# --------------------------------------------------------

# Clear Terminal
os.system("clear")

# --------------------------------------
# Instagram Profile Picture Downloader
# --------------------------------------


def Instagram():
    try:
        _extracted_from_Instagram_3()
    except il.ProfileNotExistsException as e:
        print("\033[01;31m Username does not exist ❌")
        

    except il.ConnectionException as e:
        print("\033[01;31m Connection Error 🔥")


def _extracted_from_Instagram_3():
    ig = il.Instaloader()
    user = input("\033[01;36m\nEnter Username 👤: ").strip()
    ig.download_profile(user, profile_pic_only=True)
    print("\033[01;32m Downloaded Profile Picture ✔")

# ----------------------------------------
# Instagram Photos and Videos Downloader
# ----------------------------------------


def Instagram_Reels():
    try:
        _extracted_from_Instagram_4()
    except il.ProfileNotExistsException as e:
        print("\033[01;31m Username does not exist ❌")
        

    except il.ConnectionException as e:
        print("\033[01;31m Connection Error 🔥")


def _extracted_from_Instagram_4():
    ig = il.Instaloader()
    user = input("\033[01;36m\nEnter Username 👤: ").strip()
    ig.download_profile(user, profile_pic_only=False)
    print(f"\033[01;32m {user}All Photos and Videos Downloaded ✔")


# -----------------------------------------
#  Instagram Story Downloader
# -----------------------------------------



# -----------------------------------
# Youtube Videos Downloader
# -----------------------------------

def Youtube_Video():  # sourcery skip: extract-duplicate-method
    url = input("\033[01;32m\nEnter Youtube Video URL: ").strip()
    try:
        yt = YouTube(url)
        print(f"\nYouTube Video Title : 👉 {yt.title}")
        print(f"\nYouTube Video Thumbnail Image Link:👉 {yt.thumbnail_url}")
    except Exception:
        print("\033[01;31m\nInvalid URL ❌")

    try:
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print(f"\033[01;32m\nVideo '{yt.title}'  Downloaded successfully  ✔\n")
    except Exception:
        print("\033[01;31mDownload Failed ❌")


# --------------------------------------
#  Pinterest Image and Video Downloader
# -------------------------------------

def download_pinterest_media(output_folder="./downloads"):
    url = input("\033[01;32m\nEnter Pinterest URL: ").strip()
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the Pinterest page.")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    media_url = None

    # Check if it's a video or an image
    video_element = soup.find("meta", {"property": "og:video"})
    image_element = soup.find("meta", {"property": "og:image"})

    if video_element:
        media_url = video_element["content"]
        media_type = "video"
    elif image_element:
        media_url = image_element["content"]
        media_type = "image"
    else:
        print("No image or video found in the Pinterest page.")
        return

    # Decode the URL to handle special characters
    media_url = urllib.parse.unquote(media_url)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Extract the file name from the URL
    file_name = media_url.split("/")[-1]

    # Download the media
    response = requests.get(media_url)

    if response.status_code == 200:
        with open(os.path.join(output_folder, file_name), "wb") as f:
            f.write(response.content)
        print(f"{media_type.capitalize()} downloaded successfully.")
    else:
        print(f"Failed to download the {media_type}.")




def main():

    print("""\033[01;36mChoose Options, Like Type '1' and then hit enter!
          \033[01;36m \n1:👉 Download Instagram Profile 
          \033[01;35m \n2:👉 Download Instagram Photos and Videos 
          \033[01;31m \n3:👉 Download Youtube Videos, Title and Thumbnail
          \033[01;32m \n4:👉 Download Pinterest Image and Video
          \033[01;35m \nq:👉 Quit\n""")

    options = {
        '1': Instagram,
        '2': Instagram_Reels,
        '3': Youtube_Video,
        '4': download_pinterest_media,
    }

    while True:
        try:
            User = input('\033[01;36m\nChoose Options and Hit enter: ').strip()
            if User in options:
                options[User]()
            elif User.lower() in ['q', 'qq', 'exit']:
                print("\n \033[01;36m Thanks for using! 😉")
                break
            else:
                print(
                    "\033[01;31m\nThanks! But Sorry Please try again another command")
        except KeyboardInterrupt:
            print("\033[01;31m\nTerminated!")
            break


if __name__ == "__main__":
    main()
