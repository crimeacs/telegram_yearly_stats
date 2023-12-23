# Telegram Yearly Stats
## Overview
Telegram Yearly Stats is a Python-based tool that leverages the Pyrogram library to efficiently extract and organize message data from specified Telegram channels. It's designed for users interested in data analytics, archival, or insights related to message interactions on Telegram channels.

## Features
* Automated Data Extraction: Connects to Telegram using Pyrogram and iterates through the chat history of a specified channel.
* omprehensive Data Collection: Gathers detailed information about each message, including ID, date, text, views, shares (forwards), author, and reactions.
* JSON Data Storage: Each message's data is neatly organized into a JSON file, providing an easy-to-use format for further analysis or reporting.
* Error Handling Mechanisms: Includes basic error handling to ensure smooth operation and to log any issues encountered during data extraction.

## Prerequisites
Before running the script, ensure you have:

* Python installed on your system.
* Pyrogram library and its dependencies installed. You can install them using `pip install pyrogram`.
* Your Telegram api_id and api_hash, which can be obtained by registering your application on Telegram's API development tools.

## Usage
* Clone the repository to your local machine.
* Navigate to the repository directory.
* Run the script using `python get_stats.py`.

The script will start processing messages from the specified Telegram channel and save them in the messages directory as JSON files.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page. If you want to contribute, please open a pull request.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Artemii Novoselov
