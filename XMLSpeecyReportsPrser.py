#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from xml.etree import ElementTree
from fnmatch import fnmatch

hwpath = ["CPU", "Motherboard", "RAM", "Storage", "Operating System", "Graphics"]
root = '/home/SpeecyReports'
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

            for cores in tree.findall('./mainsection/[@title="CPU"]'):
                cvalue = cores.findall('./section/entry/[@title="Cores"]')
                for info in cvalue:
                    a = info.get('title')
                    b = info.get('value')

            for memory in tree.findall('./mainsection/[@title="RAM"]'):
                mtvalue = memory.findall('./section/entry/[@title="Total memory slots"]')
                muvalue = memory.findall('./section/entry/[@title="Used memory slots"]')
                memoryslots = memory.findall('./section/section/entry/[@title="Size"]')
                memorymanufacture = memory.findall('./section/section/entry/[@title="Manufacturer"]')
                memorybandwidth = memory.findall('./section/section/entry/[@title="Max Bandwidth"]')

                for mtinfo in mtvalue:
                    mtotalname = mtinfo.get('title')
                    mtotalvalue = mtinfo.get('value')

                for muinfo in muvalue:
                    muname = muinfo.get('title')
                    slotsusage = muinfo.get('value')

                slot = 0
                mem = ''
                for memorysize in memoryslots:
                    slot += 1
                    mem += "Slot number %s" % slot + " " + memorysize.get('value') + " " \
                           + memorymanufacture[slot - 1].get('value') + " " \
                           + memorybandwidth[slot - 1].get('value') + "\n"

            for blocks in hwpath:
                for hw in tree.findall("./mainsection/section/[@title='%s']" % blocks):
                    print("####" + blocks + "###")
                    cpu = hw.get('title')

                    if cpu == "CPU":
                        print(a + " " + b)

                    if cpu == "RAM":
                        print(mtotalname + " " + mtotalvalue)
                        print(muname + " " + slotsusage)
                        print ("%s" % mem)

                    value = hw.findall('entry')
                    for vol in value:
                        print(vol.get('title'))
print("\n")
