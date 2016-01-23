#!/usr/bin/python
# -*- coding: utf-8 -*-

# Errorcodes
errors = {'100': 'Unable to create DB: Device'}

import device_utils.cli

def error_handler(code):
    print errors[code]
    sys.exit(code)

def main():
    # Get the arguments
    args = device_utils.cli.get_args()
    if 'database' in args.commands:
        if args.deploy:
            print "Deploying a new Device DB"
            import sqldeploy
            import database.Database
            sql = database.Database.ConnectSQL(db=None)
            if not sqldeploy.create_device_db(sql):
                error_handler(100)
            sqldeploy.deploy_device(sql)
        else:
            print "The %s will be named: %s" % (system, args.name)
    
    if 'manager' in args.commands:
        pass
    
    if 'agent' in args.commands:
        pass
    
if __name__ == "__main__":
    main()
    