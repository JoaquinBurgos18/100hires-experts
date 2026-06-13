# LinkedIn Organic Content Strategy — B2B SaaS
### Research Repository | 100Hires Expert Panel

---

## What This Is

A curated research base built to extract real, operational frameworks from 10 practitioners who actually run B2B SaaS growth — not consultants who write about it.

The goal: collect enough high-signal material (LinkedIn posts + YouTube transcripts) to synthesize a practical LinkedIn content playbook for 100Hires.

**Total research collected**
- 📄 ~94,400 words of YouTube transcripts (10 videos)
- 🔗 19 LinkedIn posts manually curated across all experts
- 👥 10 practitioners across 4 strategic disciplines

---

## Expert Panel

| Expert | Role | Discipline |
|---|---|---|
| [Richard van der Blom](https://www.linkedin.com/in/richardvanderblom) | CEO, Just Connecting | LinkedIn Algorithm |
| [Amanda Natividad](https://www.linkedin.com/in/amandanat/) | VP Marketing, SparkToro | Audience Research & AEO |
| [Dave Gerhardt](https://www.linkedin.com/in/davegerhardt) | Founder, Exit Five | B2B Copywriting & Brand |
| [Katelyn Bourgoin](https://www.linkedin.com/in/katebour/) | Founder, Customer Camp | Buyer Psychology |
| [Peep Laja](https://www.linkedin.com/in/peeplaja/) | Founder, Wynter & CXL | Positioning & Messaging |
| [Elena Verna](https://www.linkedin.com/in/elenaverna) | Head of Growth, Lovable | PLG & Growth Loops |
| [Udi Ledergor](https://www.linkedin.com/in/udiledergor/) | Ex-Chief Evangelist, Gong | B2B Brand Building |
| [Jason M. Lemkin](https://www.linkedin.com/in/jasonmlemkin/) | Founder, SaaStr | SaaS Metrics & Market |
| [Chris Walker](https://www.linkedin.com/in/chriswalker171/) | CEO, Encoded | Demand Generation |
| [Justin Rowe](https://www.linkedin.com/in/justin-rowe-4043339b/) | CMO, Impactable | LinkedIn Ads & ABM |

---

## Why These 10

The panel covers the full stack of LinkedIn organic growth — from how the algorithm distributes content to how buyers make decisions once they see it.

**Distribution & Algorithm**
Richard van der Blom and Amanda Natividad define the structural rules: what the algorithm rewards, how Zero-Click content works, and where audiences actually pay attention.

**Copywriting, Psychology & Positioning**
Dave Gerhardt, Katelyn Bourgoin, and Peep Laja cover why people stop scrolling, what makes ideas stick, and how to differentiate when everyone sounds the same.

**Brand & Product-Led Growth**
Elena Verna and Udi Ledergor connect top-of-funnel content to commercial outcomes — PLG activation mechanics and building a brand people remember, not just follow.

**Demand Generation & Pipeline**
Jason Lemkin, Chris Walker, and Justin Rowe anchor everything to revenue. Organic content as a distribution layer for pipeline, not a vanity metric.

---

## Repository Structure

```
/
├── research/
│   ├── sources.md                  # All 10 experts: LinkedIn, YouTube, annotations
│   ├── linkedin-posts/             # 19 posts manually curated across all experts
│   │   ├── amanda_natividad.md
│   │   ├── chris_walker.md
│   │   ├── dave_gerhardt.md
│   │   ├── elena_verna.md
│   │   ├── jason_lemkin.md
│   │   ├── justin_rowe.md
│   │   ├── katelyn_bourgoin.md
│   │   ├── peep_laja.md
│   │   ├── richard_van_der_blom.md
│   │   └── udi_ledergor.md
│   └── youtube-transcripts/        # Transcripts extracted programmatically via API
│       ├── amanda_natividad.md
│       ├── chris_walker.md
│       ├── dave_gerhardt.md
│       ├── elena_verna.md
│       ├── jason_lemkin.md
│       ├── justin_rowe.md
│       ├── katelyn_bourgoin.md
│       ├── peep_laja.md
│       ├── richard_van_der_blom.md
│       └── udi_ledergor.md
├── tools/
│   └── test_amanda.py              # Diagnostic script to validate caption availability
├── fetch_youtube_real.py           # Script used to extract YouTube transcripts
├── PROCESS.md                      # Technical log: errors, fixes, decisions
└── README.md
```

---

## How Transcripts Were Collected

YouTube transcripts were extracted programmatically using `youtube-transcript-api`. Key decisions made during execution:

- Built defensive error handling (with Claude Code) to classify and skip videos with disabled captions, rate limits, or private content — without halting the full run
- Used a hybrid approach: automated extraction for long-form video, manual curation for LinkedIn posts to avoid platform scraping penalties
- Validated caption availability per video before mass processing using an isolated test script (`/tools/test_amanda.py`)

Full technical log in [`PROCESS.md`](./PROCESS.md).

---

## Topic

**LinkedIn Organic Content Strategy for B2B SaaS**
Selected from the 100Hires research track options — chosen because it's the highest-leverage channel for the types of practitioners in this panel, and the one where the gap between generic advice and real operational insight is widest.