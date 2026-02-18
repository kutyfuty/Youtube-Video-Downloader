# 🚀 Advanced YouTube Downloader with Custom Branding

A robust YouTube video and audio downloader built with **Python**, **Flask**, and **yt-dlp**. This project was specifically optimized to bypass modern YouTube security hurdles like **PO Tokens** and **IP-based Rate Limiting** on cloud environments (VDS).

## ✨ Features
- **High-Quality Downloads:** Automatically fetches the best available video (1080p+) and audio, merging them seamlessly via FFmpeg.
- **Custom Branding:** Automatically appends `kutayonur.online` and the video resolution to every filename.
- **Smart Formatting:** Choose between MP4 video or high-quality MP3 audio.
- **Cloud Optimized:** Engineered to work on VDS environments by managing request headers and client simulations.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Engine:** yt-dlp
- **Processing:** FFmpeg (for high-def merging)
- **Frontend:** HTML5 / CSS3 / Bootstrap

## 🧩 Technical Challenges Overcome
This project was a deep dive into **Reverse Engineering** YouTube's request signatures. 
- **PO Token Management:** Implemented logic to handle Proof of Origin tokens.
- **Rate Limit Bypass:** Solved the "Format not available" issue on VDS IPs by optimizing extractor arguments and simulating clean client environments.

## 🚀 How to Run
1. Clone the repo: `git clone https://github.com/kutyfuty/Youtube-Video-Downloader.git`
2. Install dependencies: `pip install yt-dlp flask`
3. Ensure **FFmpeg** is installed on your system.
4. Run the app: `python app.py`
