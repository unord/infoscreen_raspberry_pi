from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException
import uuid
import platform
import urllib
from urllib import request
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import os
import time
import socket


class ComputerInfo:

    def __init__(self, os, macaddress, ip):
        self.macaddress = macaddress
        self.ip = ip
        self.os = os

    def get_macadress(self):

        return self.macaddress

    def get_ip(self):
        return self.ip

    def get_os(self):
        return self.os




def start_webdriver(this_platform):

    chromedriver_version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"

    if this_platform == "windows":
        this_path = "C:\\Chrome\\Chromedriver.exe"
    else:
        this_platform = os.getcwd()

    try:
        browser = webdriver.Chrome(executable_path=this_path, options=options)
    except SessionNotCreatedException:
        win_download_and_unzip(chromedriver_version_url, this_path)
        browser = webdriver.Chrome(executable_path=this_path, options=options)
    except WebDriverException:
        win_download_and_unzip(chromedriver_version_url, this_path)
        browser = webdriver.Chrome(executable_path=this_path, options=options)

    return browser


def win_download_and_unzip(chromedriver_version_url: str, extract_to='.'):
    download_url: str

    file = urllib.request.urlopen(chromedriver_version_url)
    for line in file:
        decoded_line = line.decode("utf-8")
        download_url = "https://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip".format(decoded_line)

    http_response = urlopen(download_url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)


def get_url():

    this_url = "dr.dk"
    time.sleep(900)
    return this_url

def start_webdriver():
    # Loading webdriver
    # Get webdriver from here: https://chromedriver.chromium.org/downloadsa
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = start_webdriver(ComputerInfo.computer_platform())


    browser.get(get_url())
    time.sleep(900)

def main():
    macaddress = hex(uuid.getnode())
    macaddress = ':'.join(a + b for a, b in zip(macaddress[::2], macaddress[1::2]))
    ip = socket.gethostbyname(socket.gethostname())
    os = platform.system()


    c = ComputerInfo(os, macaddress, ip)

    print(c.get_os())
    print(c.get_macadress())
    print(c.get_ip())


if __name__ == "__main__":
    main()










