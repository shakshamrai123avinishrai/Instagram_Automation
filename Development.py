import csv
import os
import time
import random
import logging
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--allow-notifications")
options.add_argument("--allow-geolocation")

driver = webdriver.Firefox(options=options)
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)

username_input = driver.find_element_by_xpath("//input[@name='username']")
password_input = driver.find_element_by_xpath("//input[@name='password']")

username_input.send_keys("your_username")
password_input.send_keys("your_password")

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
driver.implicitly_wait(10)
def crawl_explore_page(driver, num_posts_to_crawl):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(random.uniform(2,4))
    for _ in range(num_posts_to_crawl//9):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(2,4))

    post_links = driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']//a")

    csv_file = "instagram_metadata.csv"
    with open(csv_file,'w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Profile Name", "Number of Likes", "Number of Comments", "Post URL"])

        for i, post_links in enumerate(post_links[:num_posts_to_crawl]):
            post_links.click()
            time.sleep(random.uniform(2,4))

            profile_name = driver.find_element_by_xpath("//a[@class='sqdOP yWX7d     _8A5w5   ZIAjV ']").text
            num_likes = driver.find_element_by_xpath("//div[@class='Nm9Fw']/button/span").text
            num_comments = driver.find_element_by_xpath("//div[@class='Nm9Fw']/button[2]/span").text
            post_url = driver.current_url

            writer.writerow([profile_name, num_likes, num_comments, post_url])
            driver.find_element_by_xpath("//button[@class='ckWGn']").click()
            time.sleep(random.uniform(2, 4))

            writer.writerow([profile_name, num_likes, num_comments, post_url])
            driver.find_element_by_xpath("//button[@class='ckWGn']").click()
            time.sleep(random.uniform(2, 4))

def download_images_from_csv(csv_file):
    if not os.path.exits("downloaded_images"):
        os.makedirs("downloaded_images")

        logging.basicConfig(filename='download_errors.log', level=logging.ERROR)

        with open(csv_file,'r',newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    image_name = f"{row['Profile Name']}_{row['Number of Likes']}_{row['Number of Comments']}.jpg"
                    image_path = os.path.join("downloaded_images", image_name)

                    urllib.request.urlretrieve(row['Post URL'], image_path)
                    time.sleep(random.uniform(2, 4))
                    print(f"Image downloaded: {image_name}")
                except Exception as e:
                    logging.error(f"Error downloading image: {image_name} - {str(e)}")



def main(driver,num_posts_to_crawl):
    crawl_explore_page(driver, num_posts_to_crawl)
    csv_file = "instagram_metadata.csv"
    download_images_from_csv(csv_file)


    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--allow-notifications")
    options.add_argument("--allow-geolocation")

    driver = webdriver.Firefox(options=options)
    num_posts_to_crawl = 10
    main(driver, num_posts_to_crawl)

driver.quit()
