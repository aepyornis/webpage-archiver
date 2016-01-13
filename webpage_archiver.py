#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Archives webpages using wkhtmltopdf
# Check out: http://wkhtmltopdf.org/

import argparse
import subprocess

ARCHIVE_DIRECTORY = '/path/to/archive/'

parser = argparse.ArgumentParser(description='HTML to PDF')
parser.add_argument('url', help='website to download')
args = parser.parse_args()

def url_to_filepath (url):
    end_of_url = url.split('/')[-1].replace('.html', '')
    return ARCHIVE_DIRECTORY + end_of_url + '.pdf'

def command (url):
    return ['wkhtmltopdf', url, url_to_filepath(url)]

if __name__ == '__main__':
    cmd = command(args.url)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p.wait()
