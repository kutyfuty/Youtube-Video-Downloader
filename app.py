import os
import time
import threading
import yt_dlp
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# --- CONFIGURATION ---
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


def delayed_delete(file_path):
    """Wait 30 seconds and then remove the file from the server."""
    time.sleep(30)
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"🗑️ Cleanup Successful: {file_path}")
    except Exception as e:
        print(f"⚠️ Cleanup Error: {e}")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("youtube_url")
        format_selection = request.form.get("format_selection")

        ydl_opts = {
            # Branding: Title - Website - Resolution.Extension
            'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s - kutayonur.online - %(resolution)s.%(ext)s',
            'noplaylist': True,
            'ignoreerrors': True,
            'quiet': False,
        }

        if format_selection == "mp3":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            # Merges best video and best audio into a single MP4 container
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            ydl_opts['merge_output_format'] = 'mp4'

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"🚀 Processing: {video_url}")
                info_dict = ydl.extract_info(video_url, download=True)

                if info_dict is None:
                    return "Error: Could not retrieve video data."

                file_path = ydl.prepare_filename(info_dict)

                if format_selection == "mp3":
                    file_path = file_path.rsplit('.', 1)[0] + '.mp3'
                elif format_selection == "mp4" and not file_path.endswith('.mp4'):
                    file_path = file_path.rsplit('.', 1)[0] + '.mp4'

            threading.Thread(target=delayed_delete, args=(file_path,)).start()
            return send_file(file_path, as_attachment=True)

        except Exception as e:
            print(f"❌ System Error: {e}")
            return "An internal error occurred. Please try again later."

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)