from urllib.request import urlopen
from urllib.parse import urlparse
from workfiles.linkgetter import *
from workfiles.createdir import *


class Crawler:
    # class Spider:
    # initiate the global variables for this class
    proj_name = ''
    base_url = ''
    domain_name = ''
    # getting the domain name to build a condition to prevent
    # the Crawler to crawl any other domain other than the base_url
    queue_file = ''
    scraped_file = ''
    queue = set()
    scraped = set()

    def __init__(self, proj_name, base_url, domain_name):
        Crawler.proj_name = proj_name
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = Crawler.proj_name + '/getURL.txt'
        Crawler.scraped_file = Crawler.proj_name + '/setURL.txt'

        self.crawlerStart()
        self.crawl_page('Crawler 1', Crawler.base_url)

    @staticmethod
    def crawlerStart():
        '''
        start the project by creating:
        project name ---> folder name for the project
        data files   ---> getURL.txt and setURL.txt
        and write the base_url to the getURL.txt
        (set)s       ---> for the getURL.txt and setURL.txt
        add the data from getURL.text to its (set)
        '''
        create_proj_dir(Crawler.proj_name)
        create_data_files(Crawler.proj_name, Crawler.base_url)
        Crawler.queue = file_to_set(Crawler.queue_file)
        Crawler.scraped = file_to_set(Crawler.scraped_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        '''
        check if the page_url is not in the setURL.text then:
        1- Start the crawler and print to the user the steps
        2- Remove the crawled page_url from getURL.txt(file).
        3- Get the links from the crawler and add it to the
        setURL.text(set)
        4- Write it to setURL.text(file).
        '''
        if page_url not in Crawler.scraped:
            print(thread_name + 'is Crawling' + page_url)
            print('Queue' + str(len(Crawler.queue)))
            print('Finished' + str(len(Crawler.scraped)))

            Crawler.add_links_to_queue(Crawler.get_links(page_url))

            Crawler.queue.remove(page_url)
            Crawler.scraped.add(page_url)

            Crawler.write_to_files()

    @staticmethod
    def get_links(page_url):
        '''
        get the page_url and check if it HTML or not,
        then decode it to specific format and call the LinkGetter
        to get the ( <a href='#> ) only from the HTML
        '''
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            getter = LinkGetter(Crawler.base_url, page_url)
            getter.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()

        return getter.page_links()

    @staticmethod
    def add_links_to_queue(links):
        '''
        check if the link is found in getURL.tex(set)
        and setURL.tex(set) NOW or not,
        and check if the domain_name is the same in all links or not
        then add the link to getURL.tex(set)
        '''
        for link in links:
            if (link in Crawler.queue) or (link in Crawler.scraped):
                continue

            if Crawler.domain_name != get_domain_name(link):
                continue

            Crawler.queue.add(link)

    @staticmethod
    def write_to_files():
        '''
        write the data from the (set)s to the files associated with it
        '''
        set_to_file(Crawler.queue, Crawler.queue_file)
        set_to_file(Crawler.scraped, Crawler.scraped_file)


def get_domain_name(link):
    '''
    get the domain name from the link
    '''
    try:
        result = get_sub_domain_name(link).split('.')
        return result[-2] + '.' + result[-1]
    except:
        return ''


def get_sub_domain_name(link):
    '''
    catch the sub domain name from the link
    '''
    try:
        return urlparse(link).netloc
    except:
        return ''
