from html.parser import HTMLParser
from urllib import parse


class LinkGetter(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    def handle_startendtag(self, tag, attrs):
        '''
        getting the statring tags from HTML pages
        which may contain the ( <a href='#> )
        '''
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
                    # this to add the (url) to the (set) that will write to (setURL.txt)

    def page_links(self):
        '''
        return the saved data (set)
        '''
        return self.links
