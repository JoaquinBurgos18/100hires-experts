import os
from youtube_transcript_api import YouTubeTranscriptApi

EXPERTS = [
    {"name": "Chris Walker",         "file": "chris_walker.md",         "id": "_kSkVZxwtW0"},
    {"name": "Dave Gerhardt",        "file": "dave_gerhardt.md",        "id": "lOBVe0M2DaE"},
    {"name": "Richard van der Blom", "file": "richard_van_der_blom.md", "id": "nmPGcQvDnEg"},
    {"name": "Elena Verna",          "file": "elena_verna.md",          "id": "2wdsNwPUCgQ"},
    {"name": "Justin Rowe",          "file": "justin_rowe.md",          "id": "7ec3mQPwZng"},
    {"name": "Amanda Natividad",     "file": "amanda_natividad.md",     "id": "gK-f80dTjxM"},
    {"name": "Peep Laja",            "file": "peep_laja.md",            "id": "F25QDJhbhgU"},
    {"name": "Katelyn Bourgoin",     "file": "katelyn_bourgoin.md",     "id": "visxE6Tj_Mc"},
    {"name": "Udi Ledergor",         "file": "udi_ledergor.md",         "id": "HqlaUdpOgCU"},
    {"name": "Jason Lemkin",         "file": "jason_lemkin.md",         "id": "RZYUn_ExLBY"},
]

LANGS = ["en", "en-US", "en-GB"]


def fetch_transcript(video_id):
    api = YouTubeTranscriptApi()
    try:
        tl = api.list_transcripts(video_id)
        try:
            return tl.find_transcript(LANGS).fetch()
        except Exception:
            pass
        try:
            return tl.find_generated_transcript(LANGS).fetch()
        except Exception:
            pass
        for t in tl:
            try:
                return t.fetch()
            except Exception:
                continue
    except Exception:
        pass
    return api.fetch(video_id)


def to_text(segments):
    parts = []
    for s in segments:
        if isinstance(s, dict):
            parts.append(s.get("text", ""))
        else:
            parts.append(getattr(s, "text", str(s)))
    return " ".join(parts).replace("\n", " ")


def classify_error(e):
    msg = str(e).lower()
    if any(k in msg for k in ["disabled", "no transcript", "subtitles"]):
        return "SIN SUBTITULOS - busca otro video de este experto"
    if any(k in msg for k in ["unavailable", "private", "does not exist"]):
        return "VIDEO PRIVADO O NO DISPONIBLE"
    if "429" in msg or "too many requests" in msg:
        return "RATE LIMIT - espera 2 minutos y vuelve a intentar"
    return str(e)[:150]


def main():
    out_dir = os.path.join("research", "youtube-transcripts")
    os.makedirs(out_dir, exist_ok=True)
    succeeded, failed = [], []

    print("=" * 60)
    print("  YouTube Transcript Fetcher")
    print("=" * 60)

    for expert in EXPERTS:
        vid  = expert["id"]
        url  = f"https://www.youtube.com/watch?v={vid}"
        dest = os.path.join(out_dir, expert["file"])

        print(f"\n  {expert['name']}")

        try:
            segments = fetch_transcript(vid)
            text     = to_text(segments)
            words    = len(text.split())

            with open(dest, "w", encoding="utf-8") as f:
                f.write(f"# YouTube Transcript: {expert['name']}\n\n")
                f.write(f"| Field | Value |\n|---|---|\n")
                f.write(f"| Video ID | {vid} |\n")
                f.write(f"| URL | {url} |\n")
                f.write(f"| Word count | {words} |\n\n")
                f.write("---\n\n## Transcript\n\n")
                f.write(text)

            print(f"  OK: {words:,} palabras guardadas")
            succeeded.append(expert["name"])

        except Exception as e:
            print(f"  FAIL: {classify_error(e)}")
            failed.append(expert["name"])

    print(f"\n  Exitosos: {len(succeeded)}/10")
    print(f"  Fallidos: {len(failed)}/10")
    if failed:
        for n in failed:
            print(f"    - {n}")
    print("=" * 60)


if __name__ == "__main__":
    main()