from slackclient import SlackClient
import os
import yaml

_script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
_config_file_name = "config.yaml"
_abs_file_path = os.path.join(_script_dir, '..', _config_file_name)

# Configuration
with open(_abs_file_path) as _config_file:
    _config = yaml.load(_config_file)


class SlackAdapter:
    def __init__(self, slack_token):
        self.sc = SlackClient(slack_token)
        pass

    def get_channel_by_name(self, name):
        response = self.sc.api_call("channels.list")
        for channel in response['channels']:
            if channel['name'] == name:
                print channel

    def get_user_by_name(self, name):
        response = self.sc.api_call("users.list")
        for user in response['members']:
            if user['name'] == name:
                print user
                return user

    def send_message(self, text_prio, as_user=_config['as_user'], channel=_config['channel'], **kwargs):
        if 'text' in kwargs:
            kwargs.pop('text')
        self.sc.api_call("chat.postMessage", channel=channel,
                         as_user=as_user,
                         text=text_prio,
                         **kwargs)