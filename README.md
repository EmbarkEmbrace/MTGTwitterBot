<h1>MTG Twitter Bot</h1>

<h2>What It Does:</h2> - Creates a Twitter bot that pulls a random card image from Scryfall's API and posts it.

<h2>Purpose:</h2> - The purpose of this project was to develop a better understanding of APIs as well as Google Cloud.

<h2>Tech Used:</h2> - Python, APIs, Google Functions, Google Scheduler.

<h2>How It Works:</h2> - The bot generates a random number between a specified range, tacks it on to the end of Scryfall's multiverse ID endpoint, downloads the file to the local tmp directory (setup for Google Functions), and then proceeds to post the image.

<h2>Notes:</h2> - The bot is setup for Google Functions. Should you wish to launch and test the bot locally, simply adjust the key/token/secret variables, and adjust the image directory to simply be the image name while including a file name variable for the image. Alternatively, you can check out the CardAPI.py file for an example on  how the image API call to Scryfall works.
