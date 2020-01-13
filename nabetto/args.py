import argparse

parser = argparse.ArgumentParser()
required_args = parser.add_argument_group('first-time arguments')

# TODO: Check the format of the key being passed and raise an error if it's not passed correctly

required_args.add_argument('-k', '--key',
    help='Place your Riot API key after this flag',
    type=str,
    dest='key',
    metavar='API key')

required_args.add_argument('-u', '--user',
    help='Your Twitch username',
    type=str,
    dest='user',
    metavar='username')

required_args.add_argument('-p', '--passwd',
    help='Your Twitch Oath Token',
    type=str,
    dest='passwd',
    metavar='password')

parser.add_argument('-d', '--debug',
    help='''Determines what messages will print to the console. The higher the number, the less messages that will get printed.\n
    Debug 1, Info 2, Warning 3, Error 4, Critical 5''',
    type=int,
    dest='loglvl',
    metavar='level',
    choices=range(1,6),
    default=3)

parser.add_argument('-f', '--file',
help='The file to store the logs in',
dest='logpath',
metavar='file',
default=None)

parser.add_argument('-v', '--verbose',
                    help='Displays all messages',
                    action='store_true')

parser.add_argument('-s', '--save',
                    help="Saves your credentials so that you don't have to keep entering them.",
                    action='store_true',
                    dest='save_creds')

ARGS = parser.parse_args()