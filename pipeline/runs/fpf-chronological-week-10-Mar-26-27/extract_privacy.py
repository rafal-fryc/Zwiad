import sys
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.current_href = None
        self.links = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, val in attrs:
                if name == 'href':
                    self.current_href = val

    def handle_endtag(self, tag):
        if tag == 'a':
            self.current_href = None

    def handle_data(self, data):
        stripped = data.strip()
        if stripped:
            if self.current_href:
                self.links[stripped] = self.current_href
            self.text.append(stripped)

with open('/home/rafal/projecty/Zwiad/pipeline/runs/fpf-chronological-week-10-Mar-26-27/emails/FPF-U.S.-Privacy-Legislation-Updates-March-27.html') as f:
    content = f.read()

parser = TextExtractor()
parser.feed(content)
print('LINKS:')
for text, href in parser.links.items():
    print(f'  [{text}] -> {href}')
print('TEXT:')
print('\n'.join(parser.text))
