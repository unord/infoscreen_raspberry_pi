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
import xlrd

excelfile_infoscreen_info = "data.xls"


class ComputerInfo:

    def __init__(self, hostname:str, os:str, macaddress:str, ip:str):
        self.macaddress = macaddress
        self.ip = ip
        self.os = os
        self.hostname = hostname

    def get_hostname(self):
        return self.hostname

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


def win_download_and_unzip(chromedriver_version_url:str, extract_to='.'):
    download_url:str

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

def excel_infoscreen_get_sharepoint_screen(macAddress: str):

    wb = xlrd.open_workbook(excelfile_infoscreen_info)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    item_found = False
    this_hostname = ""
    this_os = ""
    this_macAddress= ""
    this_ip = ""

    for i in range(sheet.nrows):
        if macAddress in sheet.cell_value(i, 2):

            item_found = True

            this_hostname = sheet.cell_value(i, 0)
            this_os = sheet.cell_value(i, 1)
            this_macAddress = sheet.cell_value(i, 2)
            this_ip = sheet.cell_value(i, 3)

            if this_ip != C.get_ip():
                print("ip_error")
            else:
                print("ip_correct")


        if item_found == False:
            print("mac_correct")
        else:
            print("mac_error")

    return this_hostname, this_os, this_macAddress, this_ip


def main():
    macaddress = hex(uuid.getnode())
    macaddress = ':'.join(a + b for a, b in zip(macaddress[::2], macaddress[1::2]))

    macaddress = str(macaddress)
    ip = socket.gethostbyname(socket.gethostname())
    os = platform.system()
    hostname = socket.gethostname()

    global C
    C = ComputerInfo(hostname, os, macaddress, ip)

    print(C.get_hostname())
    print(C.get_os())
    print(C.get_macadress())
    print(C.get_ip())
    #excelfile_infoscreen_info(macaddress)



if __name__ == "__main__":
    main()










