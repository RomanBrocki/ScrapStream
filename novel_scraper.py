import time
import os
from shutil import copyfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from docx import Document
from pattern import pattern
from pattern import replacement
import streamlit as st

class NovelScraper:
    def __init__(self):
        self.ebook_name = ""
        self.start_url = ""
        self.end_url = ""
        self.occurrence_list = []
        self.occurrences = 0
        self.save_path = ""
        self.profile = r"c:\Users\Roman\AppData\Local\Google\Chrome\User Data\Profile Selenium"

    def check_captcha(self, browser):
        """
        Checks if a CAPTCHA is present and waits for manual resolution.
        """
        while True:
            try:
                captcha = browser.find_elements(By.CLASS_NAME, 'g-recaptcha')
                if captcha:
                    print("Captcha detected! Solve it manually and press Enter to continue...")
                    input("Press Enter after solving the Captcha...")
                    time.sleep(5)  # Extra wait time for page reload
                else:
                    break
            except:
                break

    def scrape_chapters(self, start_url, end_url):
        self.start_url = start_url
        self.end_url = end_url
        options = Options()
        options.add_argument("user-data-dir=" + self.profile)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        document = Document()
        document.save(os.path.join(self.save_path, 'Novel.docx'))

        while True:
            browser.get(self.start_url)
            self.check_captcha(browser)
            
            try:
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'chr-text')))
                title = browser.find_element(By.CLASS_NAME, 'chr-text')
                content = browser.find_element(By.ID, 'chr-content')
            except:
                print("Error loading page or elements not found. Retrying...")
                time.sleep(5)
                continue
            
            document = Document(os.path.join(self.save_path, "Novel.docx"))
            chapter_text = content.text
            
            for element in pattern:
                if element in chapter_text:
                    self.occurrence_list.append(f'Found: {element}')
                    self.occurrences += 1
                chapter_text = chapter_text.replace(element, replacement)
            
            document.add_paragraph(title.text)
            document.add_paragraph(chapter_text)
            document.add_page_break()
            document.save(os.path.join(self.save_path, "Novel.docx"))

            if self.start_url == self.end_url:
                break
            try:
                link = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'next_chap')))
                self.start_url = link.get_attribute('href')
            except:
                print("Next chapter not found. Stopping...")
                break

        browser.quit()

    def get_log(self):
        log_list = ['List of found occurrences:']
        for occurrence in self.occurrence_list:
            log_list.append(occurrence)
        log_list.append(f'Total occurrences found: {self.occurrences}')
        return log_list

    def save_ebook(self, save_path, ebook_name):
        self.ebook_name = ebook_name
        self.save_path = save_path
        os.rename(os.path.join(self.save_path, "Novel.docx"), os.path.join(self.save_path, f"{self.ebook_name}.docx"))

    def run_scraper(self, ebook_name, save_path, start_url, end_url):
        self.save_path = save_path
        self.scrape_chapters(start_url, end_url)
        self.save_ebook(save_path, ebook_name)




