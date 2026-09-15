# Profile maintenance

## Edit points

- Preserve the original profile design from commit `67d07d6`: banner, summary
  table, section order, badge rows, architecture diagram and visible stats.
  Update content inside those sections; do not redesign without an explicit
  request. Experience and education belong in the existing terminal block;
  real projects belong in the existing Featured Builds table.
- The activity graph image is the approved exception: its former Vercel host
  returned HTTP 402 / DEPLOYMENT_DISABLED. `assets/activity-graph.svg` now serves
  that same graph slot, keeping the dark background, green line and blue points.
  `scripts/update_activity_graph.py` uses GitHub's public contribution calendar,
  never guesses missing counts, and retains the previous image on fetch/parse
  failure. The existing 12-hour workflow refreshes it alongside the blog feed.
  This is a snapshot, not a real-time counter; today's counts may be incomplete.
- `README.md`: public biography, employment, projects, skills, contact links.
- `jamie10x-os.svg`: original editable terminal-style banner. Keep essential
  information as README text too, so mobile and screen-reader users can read it.
- `assets/resumes/`: the same English, Uzbek and Russian PDFs served by the
  portfolio. Do not hand-edit separate copies here.
- The existing Android blog workflow owns only the text between
  `START_SECTION:learn` and `END_SECTION:learn`. Keep both markers unchanged.
  The reading feed does not imply authorship or professional experience.

## Keeping the portfolio and profile aligned

The portfolio is the source of truth for personal content. Update its constants
first, generate all three PDFs, then update this README and copy the PDFs here.
Employment dates are not project launch dates. Do not add unverified metrics,
private repository URLs, or a guessed portfolio domain.

The owner-confirmed portfolio URL is `https://jamshiddev.uz`.

In the portfolio checkout:

```sh
python3 scripts/create-resume.py --all
python3 scripts/create-resume.py --all --check
```

Visually inspect all three rendered PDFs. Copy
`public/jamshidbek-boynazarov-resume-{en,uz,ru}.pdf` to this repository's
`assets/resumes/`. The generator requires npm dependencies, reportlab, pypdf
and Arial; its `--font-dir` option supports other font locations.

From this profile checkout, with the portfolio at its current sibling location:

```sh
python3 scripts/check-profile.py --portfolio ../glasscube-main
python3 -m unittest discover -s scripts -p 'test_*.py'
git diff --check
git diff -- README.md jamie10x-os.svg
git status --short
```

The check first verifies the original banner and visual sections against Git
history (allowing only the approved graph URL replacement), then compares
identity, employment dates, project statuses, public links,
project stacks, language proficiency and all three PDF files against the actual
portfolio constants. Pass another path to `--portfolio` if the checkout moves.
Without that option it checks local assets and preservation of the original
design only. Retain Git history when running the design check.

Review changes before staging or publishing. Updating these local files does
not change the public GitHub profile until the repository changes are pushed.
The blog workflow and its schedule are preserved; no workflow run is required
to publish manually reviewed README changes.
