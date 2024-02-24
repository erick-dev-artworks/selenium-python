from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import os
from time import sleep

#os.environ['MOZ_HEADLESS'] = '1'

#SHC INSTAGRAM BOT V-1.0.0 ( HASHTAG LIKER TURBO PUSKA )
# INSTAGRAM BOT LIKE PER HASHTAG MIN TIME TO WORK -0.1 SEC
def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(10)
        login_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
        login_button.click()
        time.sleep(10)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(10)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")

        try:
            sleep(random.randint(5, 7))
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            hrefs_in_view = [elem.get_attribute('href')
                             for elem in hrefs_in_view
                             if '/p/' in elem.get_attribute('href')]

            #Removing the top 9 posts.
            hrefs_in_view = hrefs_in_view[9:]

        except Exception as e:
            print(e)

        # Liking photos
        total_photos = len(hrefs_in_view)
        for pic_href in hrefs_in_view:
            driver.get(pic_href)
            time.sleep(2)
            sleep(random.randint(1, 3))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(random.randint(1, 3))
            driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
            try:
                sleep(random.randint(2, 4))
                check_like = driver.find_element_by_xpath("//button[normalize-space(@class)='wpO6b']/*[name()='svg']")

                #Checking if the photo is not liked previously.
                if check_like.get_attribute('aria-label') == 'Like':
                    driver.find_element_by_xpath('//span[@aria-label="Like"]').click()

                total_photos -= 1
                for second in reversed(range(0, random.randint(20, 30))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(total_photos) + " | Sleeping " + str(second) + " | ")
                    sleep(10)

            except Exception as e:
                sleep(10)

if __name__ == "__main__":
    
    #Instagram Login :

    #Enter your username here
    username = "world_record_dodgecoin"
    #Enter your password hereshitcoinexchange
    password = "ShitcoinEther11"

    ig = InstagramBot(username, password)
    ig.login()

    # Type your hashtags here as many you want :

    #Enter hashtags here
    hashtags = ['moscow', 'santpeterburg',  'chelyabinsk', 'California', 'texas', 'miami', 'princess', 'dog', 'love', 'santpeterburg', 'elonmusk', 'crypto', 'milan']
   

    while True:
        try:
            # Pick up a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()
