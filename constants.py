# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 08:16:12 2021

@author: Me
"""

footer_threshold = .20      # footer content will be looked for  in the lower %value of the page
header_threshold = .20      # header content will be looked for  in the higher %value of the page
dispalcement_treshold = 15  # how much two header or footer items can vary in position in different pages
text_distance_threshod = 2 # how much simialriy between text makes them similar (this is actually distance, so smaller is more similar )
header_footer_decision_value = 3  # if the number of similiar boxes is greated than this value, its header or footer
Min_acceptable_pages = 3



rejection_list = ['yes','no','none','none\n','yes\n','no\n','No.','None.','No.\n','None.\n']

