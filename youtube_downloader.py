import yt_dlp

url = input("Enter YouTube video URL: ")

ydl_opts = {
    'format': 'best',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("⬇ Downloading video...")
        ydl.download([url])

    print("✅ Download completed!")

except Exception as e:
    print("❌ Error:", e)