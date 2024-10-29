import requests
import time

# Read tokens and integrity data from 'int_tokens.txt'
def load_tokens():
    with open('int_tokens.txt', 'r') as file:
        tokens = [line.strip().split(':') for line in file.readlines()]
    return tokens

# Dont ask me Why i add msgs
print("[+] Start Getting Account/Create sessions 🤖")

time.sleep(2)

# Loae The File  Idk Bruh
tokens_data = load_tokens()
if tokens_data:
    print("➤ @ Type Your Streamer User ID To Start Spam Chat:")
    streamer_id = input("Enter the Streamer User ID: ")

    for access_token, client_integrity in tokens_data:
        headers = {
            'authority': 'gql.twitch.tv',
            'accept': '*/*',
            'accept-language': 'en-GB',
            'authorization': f'OAuth {access_token}',
            'client-id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
            'client-integrity': client_integrity,
            'client-session-id': '395f7f3ef2e09ee1',
            'client-version': '2ef3911f-9b4b-4757-8b92-a081a86ae03d',
            'content-type': 'text/plain;charset=UTF-8',
            'origin': 'https://m.twitch.tv',
            'referer': 'https://m.twitch.tv/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'useragent',
            'x-device-id': 'VNwu0VNCnd4kIKfyzFIzJBsSLIssjlgq'
        }

        data = [
            {
                "operationName": "FollowButton_FollowUser",
                "variables": {
                    "input": {
                        "disableNotifications": False,
                        "targetID": streamer_id
                    }
                },
                "extensions": {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"
                    }
                }
            }
        ]

        response = requests.post('https://gql.twitch.tv/gql', headers=headers, json=data)

        # Display response if successful
        if response.status_code == 200:
            print("Viewers: [placeholder for live viewer count]")
            print("Chat Live View: [placeholder for live chat data]")
            print("Name Streamer Bio: [placeholder for streamer's bio]")
            
            message = input("➤ TYPE YOUR MESSAGE: ")
            num_messages = input("➤ TYPE HOW MUCH U NEED TO SENT TO STREAMER THE MSG?: ")
            
            print(f"Sending {num_messages} messages: '{message}' to streamer with ID {streamer_id}.")
        else:
            print("Failed to retrieve data, please check tokens and streamer ID.")

else:
    print("No tokens found. Please check your 'int_tokens.txt' file format.")
