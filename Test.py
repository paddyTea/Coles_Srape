import requests
from bs4 import BeautifulSoup
import pickle
import re
from goodsClass import Good
import goodsClass
from pathlib import Path

filename = "HTML_Storage_Page_DownDown1"
try:
    with open(Path(__file__).parent/"HTMLStorage"/filename, "rb") as file:
        type(pickle.load(file))
        HTMLStorage = pickle.load(file)
        print(f"Success loading {filename}.")
except Exception as e:
    print(f"Error loading object: {e}")

soup = HTMLStorage