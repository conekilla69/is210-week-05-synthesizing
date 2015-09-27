#!usr/bin/env python
#-*- coding: utf-8 -*-
"""This returns the current date."""


from datetime import datetime


CURDATE = None
def get_current_date():
    date = datetime.date.today()
    if __name__=='__main__':
        return CURDATE
    print CURDATE
    
