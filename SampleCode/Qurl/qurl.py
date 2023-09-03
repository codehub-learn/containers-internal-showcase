import requests
import argparse


def parse_url(url):
    r = requests.get(url)
    print(r.text)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', action="store")
    args = vars(parser.parse_args())
    url = args["url"]
    parse_url(url)

if __name__=="__main__":
    main()