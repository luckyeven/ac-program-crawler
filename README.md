# Web Scraping Algonquin College Program Information with Selenium  
This is a Python script that scrapes program information from Algonquin College's website (https://www.algonquincollege.com/future-students/programs/). The script utilizes Selenium for web scraping and pandas for data manipulation. The resulting data is saved in a CSV file.  
### Example of partial data scrapped.
[result_partial.csv](https://github.com/luckyeven/ac-program-crawler/files/10980747/result_partial.csv)


## Warning  

Please be aware that web scraping may be against the terms of service of some websites. It is your responsibility to ensure that you have the right to access and scrape the target website. Additionally, websites may change their structure at any time, which could break the functionality of this script. Be respectful when using web scraping scripts, and do not overload the server with excessive requests.  

Always review the target website's robots.txt file to ensure that you are following the rules and guidelines set by the website administrators. Keep in mind that using a web scraper might have legal implications, depending on the target website's terms of service and the jurisdiction in which you are operating.  

---
```
User-agent: *
Disallow: /calendar/action~posterboard/
Disallow: /calendar/action~agenda/
Disallow: /calendar/action~oneday/
Disallow: /calendar/action~month/
Disallow: /calendar/action~week/
Disallow: /calendar/action~stream/
Disallow: /calendar/action~undefined/
Disallow: /calendar/action~http:/
Disallow: /calendar/action~default/
Disallow: /calendar/action~poster/
Disallow: /calendar/action~*/
Disallow: /*controller=ai1ec_exporter_controller*
Disallow: /*/action~*/
Disallow: /events/action~posterboard/
Disallow: /events/action~agenda/
Disallow: /events/action~oneday/
Disallow: /events/action~month/
Disallow: /events/action~week/
Disallow: /events/action~stream/
Disallow: /events/action~undefined/
Disallow: /events/action~http:/
Disallow: /events/action~default/
Disallow: /events/action~poster/
Disallow: /events/action~*/
```
The robots.txt file from AC website, which is used by website administrators to provide guidelines to web crawlers (e.g., search engine bots, web scrapers) about which sections of the website should not be accessed or indexed. This particular robots.txt file has the following rules:

* User-agent: * - The rules specified apply to all user-agents (web crawlers, scrapers, and bots).
* The Disallow lines specify the paths or patterns that are not allowed to be accessed by web crawlers. In this case, several calendar and event-related paths are disallowed.  

Here is a breakdown of the rules:

* Disallow crawling of various calendar actions, such as posterboard, agenda, one day, month, week, stream, undefined, and default views.
* Disallow crawling of any URL containing controller=ai1ec_exporter_controller.
* Disallow crawling of any URL containing /action~.
* Disallow crawling of various event actions, similar to the calendar actions, including posterboard, agenda, one day, month, week, stream, undefined, and default views.

## Features 
* Scrapes program general information, including the name, link, area of interest, campus, credential, and length.  
* Extracts additional information and learning outcomes for each program.  
* Saves the scraped data into a CSV file.  

## Requirements  
* Python 3.x
* Selenium
* Pandas
* Chrome WebDriver

## Installation
1.Clone the repository: 
```Bash
git@github.com:luckyeven/ac-program-crawler.git
```
2. Download the appropriate Chrome WebDriver for your system from [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/chromium.org/driver/) and place the chromedriver file in the project directory.
## Usage
Run the script:
```Bash
python3 ac_spider.py
```
The script will start scraping the program information and save the results in a CSV file called result.csv in the project directory.

