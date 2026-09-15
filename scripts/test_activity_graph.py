"""Regression tests for exact contribution counts and the existing chart palette."""
import unittest
from datetime import date, timedelta
from xml.etree import ElementTree

from update_activity_graph import parse_days, render


class ActivityGraphTests(unittest.TestCase):
    today = date(2026, 9, 15)

    def fixture(self):
        parts = []
        for i in range(31):
            day = self.today - timedelta(days=30-i)
            label = ['No contributions', '1 contribution', '1,234 contributions'][i % 3]
            parts.append(f'<td id="day-{i}" data-date="{day}" data-level="0"></td>'
                         f'<tool-tip for="day-{i}">{label} on September 15th.</tool-tip>')
        return ''.join(parts)

    def test_counts_come_from_tooltips_not_color_levels(self):
        days = parse_days(self.fixture(), self.today)
        self.assertEqual(len(days), 31)
        self.assertEqual([c for _, c in days[:3]], [0, 1, 1234])
        self.assertEqual(days[-1][0], self.today)

    def test_missing_day_is_not_silently_zero(self):
        with self.assertRaises(ValueError):
            parse_days(self.fixture().replace('for="day-0"', 'for="missing"'), self.today)

    def test_unexpected_response_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_days('<html>Rate limited</html>', self.today)

    def test_svg_is_accessible_and_keeps_existing_colors(self):
        svg = render(parse_days(self.fixture(), self.today))
        root = ElementTree.fromstring(svg)
        self.assertEqual(root.attrib['aria-labelledby'], 'title desc')
        ns = {'svg': 'http://www.w3.org/2000/svg'}
        self.assertEqual(len(root.findall('.//svg:circle', ns)), 31)
        for color in ['#0B0F14', '#3DDC84', '#4285F4']:
            self.assertIn(color, svg)

    def test_all_zero_days_render_without_division_by_zero(self):
        days = [(self.today - timedelta(days=30-i), 0) for i in range(31)]
        ElementTree.fromstring(render(days))


if __name__ == '__main__':
    unittest.main()
