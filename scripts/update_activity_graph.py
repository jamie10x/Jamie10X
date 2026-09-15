"""Render the last 31 days from GitHub's public contribution calendar.

No token or third-party chart host is required. Reject missing/malformed data
before touching the previous image, so a failed refresh preserves a good graph.
"""
import re
from datetime import datetime, timedelta, timezone
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://github.com/users/jamie10x/contributions'


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates = {}
        self.counts = {}
        self.tooltip = None
        self.label = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'td' and attrs.get('data-date') and attrs.get('id'):
            self.dates[attrs['id']] = datetime.strptime(attrs['data-date'], '%Y-%m-%d').date()
        if tag == 'tool-tip':
            self.tooltip = attrs.get('for')
            self.label = []

    def handle_data(self, data):
        if self.tooltip:
            self.label.append(data)

    def handle_endtag(self, tag):
        if tag == 'tool-tip' and self.tooltip:
            label = ' '.join(''.join(self.label).split())
            match = re.match(r'^(No|[\d,]+) contributions? on ', label)
            if match:
                self.counts[self.tooltip] = 0 if match[1] == 'No' else int(match[1].replace(',', ''))
            self.tooltip = None


def parse_days(html, today):
    parser = CalendarParser()
    parser.feed(html)
    counts = {day: parser.counts[key] for key, day in parser.dates.items() if key in parser.counts}
    days = [today - timedelta(days=30-i) for i in range(31)]
    if any(day not in counts for day in days):
        raise ValueError('Incomplete GitHub calendar; previous graph retained')
    return [(day, counts[day]) for day in days]


def render(days):
    width, height = 1000, 340
    left, right, top, bottom = 64, 968, 76, 262
    maximum = max(4, max(count for _, count in days))
    step = max(1, (maximum + 3) // 4)
    maximum = step * 4
    points = [(left + i * (right-left) / 30, bottom - count / maximum * (bottom-top))
              for i, (_, count) in enumerate(days)]
    line = ' '.join(f'{x:.2f},{y:.2f}' for x, y in points)
    labels = ', '.join(f'{day.isoformat()}: {count}' for day, count in days)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           '<title id="title">Jamie10X contribution activity</title>',
           f'<desc id="desc">GitHub contribution counts for the last 31 days. {escape(labels)}</desc>',
           '<rect width="100%" height="100%" rx="6" fill="#0B0F14"/>',
           '<g font-family="Arial, sans-serif" fill="#E6EDF3">',
           '<text x="64" y="34" font-size="22" font-weight="600">Contribution Activity</text>',
           f'<text x="64" y="55" font-size="12" fill="#A8B3BE">{days[0][0].isoformat()} — {days[-1][0].isoformat()} · {sum(c for _, c in days)} contributions</text>']
    for tick in range(5):
        y = bottom - tick / 4 * (bottom-top)
        svg.extend([f'<path d="M {left} {y} H {right}" stroke="#263241"/>',
                    f'<text x="52" y="{y+4}" text-anchor="end" font-size="12">{tick*step}</text>'])
    svg.extend([f'<polygon points="{left},{bottom} {line} {right},{bottom}" fill="#3DDC84" opacity="0.12"/>',
                f'<polyline points="{line}" fill="none" stroke="#3DDC84" stroke-width="2.5" stroke-linejoin="round"/>'])
    for (day, count), (x, y) in zip(days, points):
        svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3" fill="#4285F4"><title>{day.isoformat()}: {count} contributions</title></circle>')
    for i in range(0, 31, 5):
        svg.append(f'<text x="{points[i][0]}" y="286" text-anchor="middle" font-size="12">{days[i][0].strftime("%b %d")}</text>')
    svg.append('<text x="64" y="320" font-size="11" fill="#A8B3BE">Source: GitHub contribution calendar · Refreshed every 12 hours · Today may be incomplete</text></g></svg>')
    return '\n'.join(svg) + '\n'


def main():
    request = Request(SOURCE, headers={'User-Agent': 'Jamie10X-profile-graph', 'Accept-Language': 'en-US'})
    with urlopen(request, timeout=30) as response:
        html = response.read().decode('utf-8')
    days = parse_days(html, datetime.now(timezone.utc).date())
    svg = render(days)
    output = ROOT / 'assets/activity-graph.svg'
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix('.tmp')
    temporary.write_text(svg, encoding='utf-8')
    temporary.replace(output)
    print(f'Updated graph: {len(days)} days, {sum(c for _, c in days)} contributions, through {days[-1][0]}.')


if __name__ == '__main__':
    main()
