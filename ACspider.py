#import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

class ACspider(object):
    def __init__(self):
        self.url='https://www.algonquincollege.com/future-students/programs/'
        self.chromedriver='chromedriver'
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument("--window-size=1920,1200")
    def get_html(self, url,save_file=False):       

        browser=webdriver.Chrome(options=self.options, executable_path = self.chromedriver)
        browser.get(url)
        
        if save_file:
            filename = 'result.html'
            with open(filename,'w', encoding='utf-8') as f:
                f.write(browser.page_source)
      
        return browser
    
    def grab_secondary_info(self, df):
        additional_info = []

        for link in df.Link:
            print("grabbing: {}#additional-information".format(link))
            p = ""
            browser = self.get_html(link+str("#additional-information"))
            more_info = browser.find_elements(By.XPATH, '//*[@id="additional-information"]//p')
            for sentence in more_info:        
                p += str(sentence.text)
            additional_info.append({
            'Additional-information' : p
            })
        df2 = pd.DataFrame(additional_info)
        df = pd.concat([df, df2], axis=1)

        learning_outcome = []

        for link in df.Link:
            print("grabbing: {}#learning-outcomes".format(link))
            p = ""
            browser = self.get_html(link+str("#learning-outcomes"))
            more_info = browser.find_elements(By.XPATH, '//*[@id="learning-outcomes"]/ol')
            for sentence in more_info:        
                p += str(sentence.text)
            learning_outcome.append({
            'Learning-Outcome' : p
            })
            

        df3 = pd.DataFrame(learning_outcome)
        df = pd.concat([df, df3], axis=1)
        print("Finished grabbing extra information...")
        return df
    
    def grab_info(self,html, save_file=True):
        print("grabbing main page information...")
        program_info = []

        program_general = html.find_elements(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody//tr/td[2]/a')
        program_Area_of_Interest = html.find_elements(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody//tr[@class="even"]/td[3] | //*[@id="DataTables_Table_0"]/tbody//tr[@class="odd"]/td[3]')
        program_Campus = html.find_elements(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody//tr[@class="even"]/td[4] | //*[@id="DataTables_Table_0"]/tbody//tr[@class="odd"]/td[4]')
        program_Credential = html.find_elements(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody//tr[@class="even"]/td[5] | //*[@id="DataTables_Table_0"]/tbody//tr[@class="odd"]/td[5]')
        program_Length = html.find_elements(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody//tr[@class="even"]/td[6] | //*[@id="DataTables_Table_0"]/tbody//tr[@class="odd"]/td[6]')

        for general, area_of_interest, campus, credential, length in zip(program_general, program_Area_of_Interest, program_Campus, program_Credential, program_Length):
            program_info.append({
                'General': general.text,
                'Link': general.get_attribute('href'),
                'Area of Interest': area_of_interest.text,
                'Campus': campus.text,
                'Credential': credential.text,
                'Length': length.text
            })

        df = pd.DataFrame(program_info)
        df = self.grab_secondary_info(df)

        if save_file:
            filename = 'result.csv'
            df.to_csv(filename, index=False, encoding='utf-8')


    def run(self):
        try:
           html=self.get_html(self.url)
           self.grab_info(html)
        except Exception as e:
            print('Error', e)

if __name__ == '__main__':
    spider=ACspider()
    spider.run()
