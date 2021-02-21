from os import path
from selenium import webdriver
from pynput.keyboard import Controller
from time import sleep
from os.path import abspath
from os import listdir
from random import randrange

def handle_upload_window(filepath: str) -> None:
    kbd = Controller()
    kbd.type(filepath)
    kbd.type('\n')


def get_creds(file: str,sep=':') -> list:
    """Grab credentials from a file and format a list with them
    Args:
        file (str): file to grab the credentials from
        sep (str, optional): separator for the pair. Defaults to ':'.

    Returns:
        list: [username,password]
    """
    f = open(file,'r')
    creds = f.readline().split(sep)
    f.close()
    return [cred for cred in creds]


def choose_image(dirpath:str,prefix='caption_',ext=".jpg") -> str:
    """Return the path of a file in dirpath

    Args:
        dirpath (str): Path of the dir to look in
        prefix (str, optional): prefix for the file. Defaults to 'caption_'.
        ext (str, optional): extension for the file. Defaults to ".jpg".

    Returns:
        str: path to the file
    """
    if dirpath[-1] != '/':
        dirpath+='/'
    return dirpath + prefix+"{:03}".format(randrange(len(listdir(dirpath))))+ext


def set_image_used(path: str) -> None:
    pass


def post(username: str,password: str, filename: str,caption: str) -> None:
    """post image to instagram

    Args:
        username (str): username or email of the account
        password (str): password for said account
        filename (str): path of the file to post
        caption (str): caption for the post
    """

    mobile_emulation = { "deviceName": "iPhone X" }
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome('assets/webdrivers/chromedriver',options=chrome_options)
    driver.get('https://www.instagram.com/accounts/login')

    ############# LOGIN ###############
    btns = driver.find_elements_by_css_selector('div div div div button')
    for btn in btns:
        if btn.text == 'Accept':
            b = btn

    b.click()
    sleep(2)
    user_input = driver.find_element_by_name('username')
    pass_input = driver.find_element_by_name('password')
    submit = driver.find_element_by_css_selector('button[type=submit]')

    user_input.send_keys(username)
    pass_input.send_keys(password)
    submit.click()

    sleep(5)
    onetap_btn = driver.find_element_by_css_selector('main div div div button')
    onetap_btn.click()

    sleep(5)
    homescreen_btns = driver.find_elements_by_css_selector('div[role=dialog] button')
    for btn in homescreen_btns:
        if btn.text == 'Cancel':
            hs_b = btn
    hs_b.click()

    ############# POST ###############
    sleep(1)
    new_post = driver.find_element_by_css_selector('svg[aria-label="New Post"]')
    new_post.click()
    sleep(1)
    handle_upload_window(filename)
    sleep(3)
    header_buttons_filters = driver.find_elements_by_css_selector('header div div button')
    for btn in header_buttons_filters:
        if btn.text == 'Next':
            next_button = btn
    next_button.click()
    sleep(2)

    caption_textarea = driver.find_element_by_css_selector('textarea[aria-label="Write a caption…"')
    caption_textarea.send_keys(caption)

    header_buttons_caption = driver.find_elements_by_css_selector('header div div button')
    for btn in header_buttons_caption:
        if btn.text == 'Share':
            share_button = btn
    share_button.click()
    sleep(10)


def main():
    username,password=get_creds('.env')
    path = abspath('caption_images/unused')
    caption="""Abonne toi au compte @vision_exaltee pour plus de contenu !
Partage !
.
.
.
.
#visionexaltee #citation #citations #proverbe #dicton #humour #amour #pensee #image #inspiration #inspirations #phrase #phrasedujour #sensdelavie #image #tendances #texte"""

    post(username,password,path,caption)


if __name__=='__main__':
    main()