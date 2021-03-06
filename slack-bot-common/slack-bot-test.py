import os
from slackclient import SlackClient

BOT_NAME = 'slack-bot-common'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    print(api_call)

    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            print(user['name'])
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
            else:
                print("could not find bot user with the name " + BOT_NAME)
