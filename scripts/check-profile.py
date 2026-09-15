"""Read-only profile checks; optionally compare with the portfolio source."""
import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--portfolio', type=Path)
    args = parser.parse_args()
    readme = (ROOT / 'README.md').read_text()
    for marker in ['<!--START_SECTION:learn-->', '<!--END_SECTION:learn-->']:
        assert readme.count(marker) == 1, f'Missing or duplicated blog marker: {marker}'
    assert readme.index('<!--START_SECTION:learn-->') < readme.index('<!--END_SECTION:learn-->')
    assert readme.count('<details>') == readme.count('</details>')
    assert not re.search(r'Native Android App|Flutter Cross-Platform App|Backend API Service', readme)
    # Validate relative assets without contacting external services or running feeds.
    assets = re.findall(r'\]\((\./[^)]+)\)|src="(\./[^"]+)"', readme)
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
        for value in [profile['name'], profile['email'], t['title'], t['intro'],
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
            section = readme.split('### ' + project['name'] + ' · ', 1)[1].split('\n##', 1)[0]
            assert t['status'][project['status']] in section.splitlines()[0]
            for key in ['demo', 'play', 'telegram']:
                if project.get(key):
                    assert project[key] in section, f'Wrong {key} URL for {project["name"]}'
            if project['id'] != 'pic2pdf':
                for skill in project['stack']:
                    assert skill in section, f'Missing stack: {project["name"]} / {skill}'
        for level in t['languageLevels']:
            language, proficiency = level.split(' · ')
            assert f'**{language}:** {proficiency}' in readme
        for lang in ['en', 'uz', 'ru']:
            filename = f'jamshidbek-boynazarov-resume-{lang}.pdf'
            assert (ROOT / 'assets/resumes' / filename).read_bytes() == (portfolio / 'public' / filename).read_bytes(), f'Outdated PDF: {lang}'
    print('PASS: profile assets, blog markers' + (', portfolio facts and identical EN/UZ/RU PDFs.' if args.portfolio else '.'))


if __name__ == '__main__':
    main()
