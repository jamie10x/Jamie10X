# Profile maintenance

## Edit points

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
git diff --check
git diff -- README.md jamie10x-os.svg
git status --short
```

The check compares identity, employment dates, project statuses, public links,
project stacks, language proficiency and all three PDF files against the actual
portfolio constants. Pass another path to `--portfolio` if the checkout moves.
Without that option it checks local assets and README structure only.

Review changes before staging or publishing. Updating these local files does
not change the public GitHub profile until the repository changes are pushed.
The blog workflow and its schedule are preserved; no workflow run is required
to publish manually reviewed README changes.
