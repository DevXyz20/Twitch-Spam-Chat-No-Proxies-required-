import requests
import time
import json

# Read access tokens from file
def load_tokens(filename='tokensaccs.txt'):
    with open(filename, 'r') as file:
        tokens = [line.strip() for line in file if line.strip()]
    return tokens

# Set headers for Twitch GQL API
def get_headers(access_token):
    return {
        'authority': 'gql.twitch.tv',
        'accept': '*/*',
        'accept-language': 'en-GB',
        'authorization': f'OAuth {access_token}',
        'client-id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://m.twitch.tv',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

# Verify token and check access
def verify_token(token):
    headers = get_headers(token)
    print("➤ SCRAPE TWITCH GQL.. 🤖")
    time.sleep(3)
    # Sample request to verify token access
    data = [{"operationName": "FollowButton_FollowUser", "variables": {"input": {"disableNotifications": False, "targetID": "1169562962"}}, "extensions": {"persistedQuery": {"version": 1, "sha256Hash": "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"}}}]
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("\033[92m➤ ACCESS TOKENS SUCCESS VERIFIED.\033[0m")  # Green color
        return True
    else:
        print("Failed to verify token.")
        return False

# Retrieve streamer information
def get_streamer_info(channel_id, token):
    headers = get_headers(token)
    data = [
        {
            "operationName": "StreamMetadata",
            "variables": {
                "channelID": channel_id
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "sampleHash"
                }
            }
        }
    ]
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        info = response.json()
        # Display streamer information
        print(f"Bio Streamer: {info['bio']}")
        print(f"Name streamer: {info['displayName']}")
        print(f"Views: {info['viewCount']}")
        print(f"Stream Start Date: {info['createdAt']}")
        return True
    return False

# Send messages to streamer
def send_messages(token, channel_id, message, count):
    headers = get_headers(token)
    data = {
        "operationName": "SendMessage",
        "variables": {
            "channelID": channel_id,
            "message": message
        }
    }
    for i in range(count):
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Message {i+1} sent successfully.")
        else:
            print(f"Failed to send message {i+1}.")
        time.sleep(1)

# Main function
def main():
    tokens = load_tokens()
    for token in tokens:
        if verify_token(token):
            channel_id = input("➤ Enter Channel Id: ")
            if get_streamer_info(channel_id, token):
                message = input("➤ Enter Your Message to send to the streamer: ")
                count = int(input("➤ How many messages to send [MAX: 25]: "))
                if count > 25:
                    print("Maximum allowed messages is 25. Setting to 25.")
                    count = 25
                send_messages(token, channel_id, message, count)
            else:
                print("Failed to retrieve streamer info.")
        else:
            print("Invalid token, skipping.")

if __name__ == "__main__":
    main()
