#!/usr/bin/python3
"""Fetches URL status and displays response"""
import requests

url = "https://alu-intranet.hbtn.io/status"
if url.startswith('https://'):
    url = "https://alu-intranet.hbtn.io/status"

if __name__ == "__main__":
    resp = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
