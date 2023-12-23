import pandas as pd
import json
from pyrogram import Client

def main():
    api_id = 0 # e.g. 100500 (int)
    api_hash = "<YOUR HASH>" # e.g. 'sdfsdf2341142' (str)
    channel_username = "<YOU CHANNEL NAME>" # 'nn_for_science' 

    with Client("my_account", api_id, api_hash) as app:
        for message in app.get_chat_history(channel_username):
            print()
            try:
                message_id = message.id
                message_date = message.date.strftime("%Y-%m-%d %H:%M:%S") if message.date else "No date available"
                message_text = message.caption if message.caption else "No message content"
                message_views = message.views if message.views else 0
                message_forwards = message.forwards if message.forwards else 0
                message_author = message.author_signature

                # Parsing reactions
                reactions = {}
                if message.reactions and message.reactions.reactions:
                    for reaction in message.reactions.reactions:
                        reactions[reaction.emoji] = reaction.count

                # Constructing the data dictionary
                data_dict = {
                    "Date": message_date,
                    "Author" : message_author,
                    "Message": message_text,
                    "Views": message_views,
                    "Forwards (Shares)": message_forwards,
                    "Reactions": reactions,
                }

                # Saving the data to a JSON file
                with open(f'{message_id}_data.json', 'w', encoding='utf-8') as f:
                    json.dump(data_dict, f, ensure_ascii=False, indent=4)

            except Exception as e:
                print(f"An error occurred: {e}")
            # break

if __name__ == "__main__":
    main()
