import argparse

parser = argparse.ArgumentParser()
required_args = parser.add_argument_group('required arguments')

required_args.add_argument('-k', '--key',
    help='Place your Riot API key after this flag',
    type=str,
    dest='key',
    metavar='API key',
    required=True)

required_args.add_argument('-u', '--user',
    help='Your Twitch username',
    type=str,
    dest='user',
    metavar='username',
    required=True)

required_args.add_argument('-p', '--passwd',
    help='Your Twitch Oath Token',
    type=str,
    dest='passwd',
    metavar='password',
    required=True)

parser.add_argument('-d', '--debug',
    help='''Determines what messages will print to the console. The higher the number, the less messages that will get printed.\n
    Debug 1, Info 2, Warning 3, Error 4, Critical 5''',
    type=int,
    dest='loglvl',
    metavar='logging level',
    choices=range(1,6),
    default=3,
    required=False)

parser.add_argument('-f', '--file',
help='The file to store the logs in',
dest='logpath',
metavar='file',
default=None,
required=False)

parser.add_argument('-v', '--verbose',
                    help='Displays all messages',
                    action='store_true')

ARGS = parser.parse_args()