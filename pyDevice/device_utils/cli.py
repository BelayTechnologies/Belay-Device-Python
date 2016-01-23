#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

def get_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='commands', help='commands')
    
    manager = subparsers.add_parser('manager', help='Manager Commands')
    manager.set_defaults(which='manager')
    manager.add_argument('-n', '--name',
                         action='store',
                         help='The name of the manager')
    
    database = subparsers.add_parser('database', help='Database Commands')
    database.set_defaults(which='database')
    database.add_argument('-d', '--deploy',
                          action='store_true',
                          help='Deploy Device Database')
    
    agent = subparsers.add_parser('agent', help='Agent Commands')
    agent.set_defaults(which='agent')
    agent.add_argument('-n', '--name',
                       action='store',
                       help='The name of the agent')
    
    args = parser.parse_args()
    
    return args
    
if __name__ == "__main__":
    get_args()
   