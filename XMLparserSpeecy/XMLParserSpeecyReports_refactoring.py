#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from xml.etree import ElementTree
from fnmatch import fnmatch

hwpath = ["CPU", "Motherboard", "RAM", "Storage", "Operating System", "Graphics"]

details = ["Cores", "Total memory slots", "Used memory slots",
          "Size", "Manufacturer", "Max Bandwidth"]

root = '/home/Inventarization/SpeecyReports'
pattern = "*.xml"

for path, subdirs, files in os.walk(root):
          
    for name in files:
        if fnmatch(name, pattern):
            filelist = os.path.join(path, name)
            print("###########")
            print("\n")
            print(filelist)

        with open('%s' % filelist, 'rt') as f:
            tree = ElementTree.parse(f)
            for section in hwpath:
                print(section + "____________")

                for rootsection in tree.findall('./mainsection/[@title="%s"]' % section):

                    for subsection in details:

                        for hw_info in rootsection.findall('./section/entry/[@title="%s"]' % subsection):
                            print(hw_info.get('title') + ": " + hw_info.get('value'))

                        for detailed_info in rootsection.findall('./section/section/entry/[@title="%s"]' % subsection):
                            print(detailed_info.get('title') + ":" +  detailed_info.get('value'))

                ### General information ###

                for hw in tree.findall("./mainsection/section/[@title='%s']" % section):
                    for vol in hw.findall('entry'):
                        print(vol.get('title'))
print("\n")
