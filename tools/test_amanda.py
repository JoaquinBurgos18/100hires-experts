#!/usr/bin/env python3
"""
test_amanda.py

Utility script to check transcript availability for a single YouTube video
before adding it to the main fetch script.

Usage:
    1. Find a candidate video on YouTube (look for the CC button in the player)
    2. Copy the video ID from the URL (the part after ?v=)
    3. Replace REPLACE_WITH_ID below with that ID
    4. Run: python test_amanda.py

If transcripts are available, you will see a list of languages.
If not, try a different video by the same expert.
"""

from youtube_transcript_api import YouTubeTranscriptApi

# ── Replace this with the video ID you want to test ──────────────────────────
VIDEO_ID = "REPLACE_WITH_ID"
# ─────────────────────────────────────────────────────────────────────────────

def check_video(video_id):
    print(f"\nChecking: https://www.youtube.com/watch?v={video_id}\n")
    try:
        api = YouTubeTranscriptApi()
        tl  = api.list_transcripts(video_id)
        print("Transcripts available:\n")
        for t in tl:
            kind = "auto-generated" if t.is_generated else "manual"
            print(f"  - {t.language:<20} ({t.language_code})  |  {kind}")
        print("\nThis video will work with fetch_youtube_real.py")
    except Exception as e:
        msg = str(e).lower()
        if "disabled" in msg or "no transcript" in msg:
            print("No transcripts available on this video.")
            print("Try a different video by the same expert.")
        elif "unavailable" in msg or "private" in msg:
            print("Video is private or unavailable.")
        else:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if VIDEO_ID == "REPLACE_WITH_ID":
        print("Please replace REPLACE_WITH_ID with an actual YouTube video ID first.")
    else:
        check_video(VIDEO_ID)