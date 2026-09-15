"""Read-only profile checks; optionally compare with the portfolio source."""
import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check_original_design(readme):
    # The owner explicitly chose this layout. Content updates must not replace
    # its banner, section order, badges, architecture diagram or activity panels.
    baseline = subprocess.check_output(
        ['git', 'show', '67d07d6:README.md'], cwd=ROOT, text=True)
    # The sole approved image replacement: the external graph host is disabled.
    baseline = baseline.replace(
        'https://github-readme-activity-graph.vercel.app/graph?username=jamie10x&bg_color=0B0F14&color=E6EDF3&line=3DDC84&point=4285F4&area=true&hide_border=true',
        './assets/activity-graph.svg')
    original_banner = subprocess.check_output(
        ['git', 'show', '67d07d6:jamie10x-os.svg'], cwd=ROOT)
    assert (ROOT / 'jamie10x-os.svg').read_bytes() == original_banner, 'Original banner changed'
    # The scheduled reading feed owns its article heading; exclude it from the
    # layout comparison so legitimate feed updates do not break this check.
    def headings(text):
        text = re.sub(r'<!--START_SECTION:learn-->.*?<!--END_SECTION:learn-->', '', text, flags=re.S)
        return re.findall(r'^#+ .+$', text, re.M)
    assert headings(readme) == headings(baseline), 'Original section order changed'
    for start, end in [('## Tech Stack', '## Currently Syncing'), ('## Stats & Activity', '## Coding Profiles')]:
        assert readme.split(start, 1)[1].split(end, 1)[0] == baseline.split(start, 1)[1].split(end, 1)[0], f'Original visual section changed: {start}'
    assert re.findall(r'src="([^"]+)"', readme) == re.findall(r'src="([^"]+)"', baseline), 'Original images changed'
    assert '| `SYSTEM` | `VALUE` | `SYSTEM` | `VALUE` |' in readme
    assert '| Project | What I Built | Stack |' in readme


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--portfolio', type=Path)
    args = parser.parse_args()
    readme = (ROOT / 'README.md').read_text()
    check_original_design(readme)
    assert 'href="https://jamshiddev.uz"' in readme, 'Missing confirmed portfolio link'
    graph = (ROOT / 'assets/activity-graph.svg').read_text()
    assert graph.count('<circle ') == 31, 'Expected 31 daily activity points'
    for marker in ['<!--START_SECTION:learn-->', '<!--END_SECTION:learn-->']:
        assert readme.count(marker) == 1, f'Missing or duplicated blog marker: {marker}'
    assert readme.index('<!--START_SECTION:learn-->') < readme.index('<!--END_SECTION:learn-->')
    assert readme.count('<details>') == readme.count('</details>')
    assert not re.search(r'Native Android App|Flutter Cross-Platform App|Backend API Service', readme)
    # Validate relative assets without contacting external services or running feeds.
    assets = re.findall(r'\]\((\./[^)]+)\)|(?:src|href)="(\./[^"]+)"', readme)
    for markdown, html in assets:
        assert (ROOT / (markdown or html)).is_file(), f'Missing asset: {markdown or html}'
    for lang in ['en', 'uz', 'ru']:
        filename = f'jamshidbek-boynazarov-resume-{lang}.pdf'
        asset = ROOT / 'assets/resumes' / filename
        assert asset.read_bytes().startswith(b'%PDF-'), f'Invalid PDF: {filename}'

    if args.portfolio:
        portfolio = args.portfolio.resolve()
        data = json.loads(subprocess.check_output(
            ['node', str(portfolio / 'scripts/export-resume-data.mjs')],
            cwd=portfolio, text=True))
        t, profile, career = data['content']['en'], data['profile'], data['career']
        for value in [profile['name'], profile['email'], t['title'], t['degree'],
                      t['location'], t['availability'], career['tarmoqda']['company'],
                      f"{career['tarmoqda']['start']}–{t['present']}",
                      f"{career['freelance']['start']}–{career['freelance']['end']}",
                      f"{career['education']['start']}–{career['education']['end']}"]:
            assert value in readme, f'Profile differs from portfolio: {value}'
        for item in data['social']:
            if item['label'] in ['LinkedIn', 'Telegram', 'LeetCode', 'Google Developer']:
                assert item['href'] in readme, f'Missing contact link: {item["label"]}'
        for project in data['projects']:
            # Restrict each check to its project, so another card cannot mask drift.
            section = next(line for line in readme.splitlines() if line.startswith('| **' + project['name'] + '**'))
            assert len(section.split('|')) == 5, 'Featured Builds must retain its three-column table'
            assert t['status'][project['status']] in section
            for key in ['demo', 'play', 'telegram']:
                if project.get(key):
                    assert project[key] in section, f'Wrong {key} URL for {project["name"]}'
            if project['id'] != 'pic2pdf':
                for skill in project['stack']:
                    assert skill in section, f'Missing stack: {project["name"]} / {skill}'
        for level in t['languageLevels']:
            assert level in readme
        for lang in ['en', 'uz', 'ru']:
            filename = f'jamshidbek-boynazarov-resume-{lang}.pdf'
            assert (ROOT / 'assets/resumes' / filename).read_bytes() == (portfolio / 'public' / filename).read_bytes(), f'Outdated PDF: {lang}'
    print('PASS: original design, profile assets, blog markers' + (', portfolio facts and identical EN/UZ/RU PDFs.' if args.portfolio else '.'))


if __name__ == '__main__':
    main()
