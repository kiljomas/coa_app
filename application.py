#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2

This starts flask dashboard.
All the configs are in beach.config.py
Bind to PORT if defined, otherwise default to 8080
'''

from beach import application

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8080
    application.run(host='0.0.0.0', port=application.config['PORT'], debug=application.config['DEBUG'])