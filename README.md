# News Twitter Bot
Twitter bot that replies to news tweets performing search and replace from a collaborative translation table. Users can contribute to the translation table via DM or @mentions.
The translation table is then human reviewed and approved entries are appended to the production table.

## Setup with Google Cloud Platform
<img src="https://miro.medium.com/max/12516/1*CMz4r3-pEFp3Po6oHv-JxQ.png" width="350"/>

Go to the [Google Cloud Console](https://console.cloud.google.com/) to get started. Set up billing and create a new project. Don't worry about getting billed, the scale of this project should fall well inside the free tier.
Once the project is set up, go to the [Cloud Functions](https://console.cloud.google.com/functions) to begin importing the code that will be executed.
