# Research Process Log

This document tracks the real process of building this research project, including errors, debugging steps, and decisions made along the way.

---

## Day 1 — Setup & First Attempt

### Goal

Fetch YouTube transcripts from 10 B2B SaaS LinkedIn experts using the `youtube-transcript-api` Python library.

### Error 1: `list_transcripts` not found

Ran the initial script and got this across all 10 experts:

```
ERROR: type object 'YouTubeTranscriptApi' has no attribute 'list_transcripts'

```

**Root cause:** The script was written assuming an older API style. The installed version (`youtube-transcript-api 1.2.4`) moved `list_transcripts` from a class method to an instance method in its 1.x major release. The original code called `YouTubeTranscriptApi.list_transcripts(video_id)` but version 1.x requires instantiating first: `YouTubeTranscriptApi().list_transcripts(video_id)`.

---

### Error 2: `NoTranscriptAvailable` import fails

After fixing the first issue, a new error appeared on startup:

```
ImportError: cannot import name 'NoTranscriptAvailable' from
'youtube_transcript_api._errors'. Did you mean: 'TranscriptsDisabled'?

```

**Root cause:** Version 1.2.4 renamed internal exception classes. Importing from `_errors` directly is fragile because it is a private module.

**Fix:** Removed all imports from `_errors`. Replaced typed exception handling with string-based error classification — reading the error message content instead of matching the exception class name.

---

### Error 3: Downgrade to 0.6.3 broke everything

Attempted to downgrade to `youtube-transcript-api==0.6.3` for compatibility. This produced a new error across all 10 experts:

```
FAIL: no element found: line 1, column 0

```

**Root cause:** Version 0.6.3 uses XML parsing internally to fetch transcripts, and YouTube had updated their response format in a way that broke this version.

**Fix:** Upgraded back to 1.2.4 and rewrote the script to work natively with the instance-based API of that version.

---

## Final Result

```
Exitosos: 10/10
Fallidos: 0/10

```


| Expert               | Words  |
| -------------------- | ------ |
| Chris Walker         | 9,535  |
| Dave Gerhardt        | 12,939 |
| Richard van der Blom | 6,559  |
| Elena Verna          | 13,347 |
| Justin Rowe          | 7,580  |
| Amanda Natividad     | 5,934  |
| Peep Laja            | 5,363  |
| Katelyn Bourgoin     | 10,799 |
| Udi Ledergor         | 11,298 |
| Jason Lemkin         | 11,053 |


**Total: ~94,407 words of B2B SaaS LinkedIn strategy content.**

---

## Diagnostic tool created

During debugging, a utility script `test_amanda.py` was written to check transcript availability for a single video ID before running the full batch. This avoids wasting time re-downloading all 10 transcripts just to test one.

---

## Key lessons


| #   | Lesson                                                                                      |
| --- | ------------------------------------------------------------------------------------------- |
| 1   | Pin library versions in scripts (`pip freeze > requirements.txt`) to avoid breaking changes |
| 2   | Never import from private modules (`_errors`, `_internal`) — names change between versions  |
| 3   | Test a single case before running a full batch                                              |
| 4   | Downgrading is not always safer — older versions can break on updated external APIs         |
| 5   | Commit frequently with descriptive messages — the history is part of the deliverable        |


