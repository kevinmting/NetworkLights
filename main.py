import argparse

import slave
import master


def run_slave(args):
    slave.run(args.rpi)


def run_master(args):
    master.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    parser_slave = subparsers.add_parser('slave')
    parser_slave.set_defaults(func=run_slave)
    parser_slave.add_argument('--rpi', action='store_true')

    parser_master = subparsers.add_parser('master')
    parser_master.set_defaults(func=run_master)

    args = parser.parse_args()
    args.func(args)

