#!/usr/bin/env python

from bs4 import BeautifulSoup
import sys

txt = sys.stdin.buffer.read().decode().strip()
soup = BeautifulSoup(txt,'lxml')

function_names = [f'{s.a.string}\n' for s in soup.find_all("td",class_="function_name")]

for s in function_names:
    sys.stdout.buffer.write(s.encode("utf-8"))

