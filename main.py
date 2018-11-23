import argparse

import slave

def run_slave(args):
    print("slave")
    slave.app.run(host="0.0.0.0")

def run_master(args):
    print("master")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    parser_slave = subparsers.add_parser('slave')
    parser_slave.set_defaults(func=run_slave)
    
    parser_master = subparsers.add_parser('master')
    parser_master.set_defaults(func=run_master)

    args = parser.parse_args()
    args.func(args)

