# Instagram_Automation
Imports necessary libraries and modules including csv, os, time, random, logging, urllib.request, webdriver and Options from selenium.
Sets up Firefox options for Selenium WebDriver to maximize the browser window and allow notifications and geolocation.
Opens the Instagram login page and waits for it to load.
Enters the username and password and clicks on the login button.
Defines a function crawl_explore_page to crawl through the explore page, click on posts, extract metadata (profile name, number of likes, number of comments, post URL), and write the metadata to a CSV file named instagram_metadata.csv.
Defines a function download_images_from_csv to download images from the URLs in the CSV file and save them in a directory named downloaded_images. Any errors that occur during the download process are logged in a file named download_errors.log.
Defines the main function to orchestrate the crawling and downloading processes.
Calls the main function to execute the automation process.
Quits the WebDriver to close the browser window.
