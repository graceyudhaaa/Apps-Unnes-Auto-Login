# ELENA AUTO LOGIN SCRIPT

Are you tired of constantly login to elena.
Late to admit your present because logging in to elena was lame.
Too lazy to loggin? 

### **INTRODUCING ELENA AUTO LOGIN SCRIPT**

## How it works:

it essentialy just python + selenium script that can run with shell script.

## requirements

- python <= 3.7 with pip
- selenium
- web browser
- internet connection

**supported web browser:**
- Chrome == "chrome"
- Chromium == "chromium"
- FireFox == "firefox"
- IE == "ie"
- Edge == "edge"
- Opera == "opera"*

*: may result in a bug, maybe i'll fix this later

## How to use

1. clone this repository
2. open up the `settings.py` and fill in the required value (username, password, browser and webdriver version)
3. copy `run.sh/run-mac.sh` into easy to reach destination (i.e desktop) **as a shortcut**.
4. run it via the shortcut, for the first run the script will download the webdriver and stores it in cache so it will run from cache for the next execution

## Bug
- sometimes google will still want you to confirm so keep your phone with it

## Further reading and dependency
This project was made possible with Selenium and Webdriver-manager *(Thank You!)*. 

if you have any trouble with this app i would recommend to go into the source code of both this repo and dependency

- https://github.com/graceyudhaaa/Elena-Auto-login
- https://github.com/SeleniumHQ/selenium
- https://github.com/SergeyPirogov/webdriver_manager

