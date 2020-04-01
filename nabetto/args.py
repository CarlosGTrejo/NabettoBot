import argparse

parser = argparse.ArgumentParser(prog="nabetto")
required_args = parser.add_argument_group('Required arguments')

required_args.add_argument('-u', '--user',
                           help='Your Twitch username',
                           type=str,
                           dest='user',
                           metavar='username')

required_args.add_argument('-t', '--token',
                           help='Your Twitch Oath Token',
                           type=str,
                           dest='passwd',
                           metavar='password')

parser.add_argument('-d', '--debug',
                    help='''Determines what messages will print to the console. The higher the number, the less messages that will get printed.\n
    Debug 1, Info 2, Warning 3, Error 4, Critical 5''',
                    type=int,
                    dest='log_level',
                    metavar='level',
                    choices=range(1, 6),
                    default=3)

parser.add_argument('-f', '--file',
                    help='The file to store the logs in',
                    dest='logpath',
                    metavar='file',
                    default=None)

parser.add_argument('-c', '--chat',
                    help='Displays Twitch chat messages',
                    action='store_true')

parser.add_argument('-s', '--save',
                    help="Saves your credentials so that you don't have to keep entering them.",
                    action='store_true',
                    dest='save_creds')

ARGS = parser.parse_args()
