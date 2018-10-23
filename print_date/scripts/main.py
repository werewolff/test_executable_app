#!/usr/bin/env python3

import argparse

from print_date.app import app

def main():
    ex = app.App;

    parser = argparse.ArgumentParser(description='Test executable application print_date')

    parser.add_argument('--days', default=0, type=int, help='default = 0. equals now')
    parser.set_defaults(days=0)

    subparsers = parser.add_subparsers(help="date type")

    now_parser = subparsers.add_parser('now', help='print datetime.datetime.now()')
    now_parser.set_defaults(func=app.now)

    tomorrow_parser = subparsers.add_parser('tomorrow', help='print datetime.datetime.now() + 1')
    tomorrow_parser.set_defaults(func=app.tomorrow)

    yesterday_parser = subparsers.add_parser('yesterday', help='print datetime.datetime.now() - 1')
    yesterday_parser.set_defaults(func=app.yesterday)

    args = parser.parse_args()

    if 'func' in args:
        args.func()

    else:
        ex.response(args.days)


if __name__ == '__main__':
    main()
