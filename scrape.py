from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
#import selenium.webdriver as webdriver
#from selenium.webdriver.chrome.service import Service
#import time

SBR_WEBDRIVER = 'https://brd-customer-hl_8a10678a-zone_scraper:td7ei0kyeqq1@brd.superproxy.io:9515'

#Grabbing content from website
def scrape_website(website):
    print("Launching chrome browser...")
    
#            def main():
#            print('Connecting to Scrapping Browser...')
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
#                print('Connected! Navigating to https://jumia.com...')
                driver.get(website)
                #Captcha handling: If you're expecting a CAPTCHA on the target page, use the following code
                print('Waiting for captcha to solve...')
                solve_res = driver.execute('executeCdpCommand', {
                    'cmd': 'Captcha.waitForSolve'
                    'params': {'detectTimeout': 10000},     
                 })
                 print('Captcha solve status:', solve_res['value']['status'])
                print('Navigated! Scraping page content...')
                html = driver.page_source
#                print(html)
                return html
                
                
#        if __name__== '__main__':
#            main()   
#    chrome_driver_path = "./chromedriver.exe"
#   options = webdriver.ChromeOptions()
#    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)   
#    try:
#        driver.get(website)
#        print("Page loaded...")
#        html = driver.page_source
#        time.sleep(10)       
#        return html
#    finally:
#        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
        
        cleaned_content = soup.get_text(separator="\n")
        cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
        
        return cleaned_content
    
    
def split_dom_content(dom_content, max_length=7000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]    
        
        
       
        
        
        