<img src="img/banner.png" width="500"/>
# News Twitter Bot
See the bot in action here: [@ny_tames](https://twitter.com/ny_tames).

This code implements a twitter bot that replies to news tweets performing search and replace from a collaborative translation table. Users can contribute to the translation table via DM or @mentions.
The translation table `pending_dic.txt` is then human reviewed and approved entries are appended to the production table `dic.txt`.

## Setup tweepy credentials
We will be using [Tweepy](https://www.tweepy.org/) as the python twitter API library as it's easy and convenient.
After creating your bot account, go to the [Developer Twitter Page](https://developer.twitter.com/en) and apply for a developer account. Once granted generate your keys *consumer_key*, *consumer_secret*, *access_token*, *access_token_secret* and put them into the `keys.py`file.

## Setup with Google Cloud Platform
<img src="https://miro.medium.com/max/12516/1*CMz4r3-pEFp3Po6oHv-JxQ.png" width="350"/>

Go to the [Google Cloud Console](https://console.cloud.google.com/) to get started. Set up billing and create a new project. Don't worry about getting billed, the scale of this project should fall well inside the free tier.
Once the project is set up, go to the [Cloud Functions](https://console.cloud.google.com/functions) to begin importing the code that will be executed.

We will be using an HTTP trigger so whenever a request is made to the URL the function will be executed. Choose 128MiB of allocated memory since it's the smallest. Our bot is written on Python so select Python3.7 as the runtime type and `send_tweet()` as the entry point. The `send_tweet()` function inside `bot.py` will actually be the function executed. If this is your first time, you will have to enable Cloud Build API.

Next, upload the files `main.py`, `mentions.py`, `requirements.txt`, `dic.txt`, `pending_dic.txt`, select `bot` as the entry point and hit deploy. Now we have a function that gets executed everytime someone visits the HTTP trigger, it is time to create an automatic trigger.

First go into the trigger section of the function and copy the trigger URL to your clipboard. Now go into the [Google Cloud Scheduler](https://console.cloud.google.com/cloudscheduler) and Create a job, select a region. Give it a name, a UNIX crontab format and HTTP target.
