import requests
import os
import json

class FigCrawler(object):
    def __init__(self, output_root, url_list_file):
        self.output_root = output_root
        self.url_list_file = url_list_file
        self.output_folder = os.path.join(self.output_root, self.url_list_file)
        self.check_exist(self.output_folder)
        
    def check_exist(self, dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def get_url_list(self):

        with open(self.url_list_file + '.txt', 'r') as f:
            urls = [line.rstrip('\n') for line in f]

        return urls


    def record(self, info, filepath):
        txtpath = filepath[:-4] + '.json'
        with open(txtpath, 'w') as f:
            json.dump(info, f)
        print('Info saved',txtpath)
        
    def crawl(self, url, filename):
        filepath = os.path.join(self.output_folder, filename+'.jpg')
        with open( filepath , 'wb') as handle:
                response = requests.get(url, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        self.record(url, filepath)
        print('Fig  Saved', filepath)

    def run(self):
        url_list = self.get_url_list()
        for idx, url in enumerate(url_list):
            print('Crawling ', url)
            self.crawl(url, self.url_list_file + '_' + str(idx))
            print('='*80)
        
        print('All fig in {} are crawled into {}'.format(self.url_list_file, self.output_folder))




if __name__ == "__main__":
    output_root = '../output/'
    url_list_file = 'happy'
    crawler = FigCrawler(output_root, url_list_file)
    crawler.run()


