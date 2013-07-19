#-------------------------------------------------------------------------------
# Name:        json_dyn_retweet_finder
# Purpose:     parsing retweets from dynamically split snapshots
# Author:      konkonst
#
# Created:     31/05/2013
# Copyright:   (c) ITI (CERTH) 2013
# Licence:     <apache licence 2.0>
#-------------------------------------------------------------------------------
import json
import codecs
import os,glob
import csv
import wx
#User selects folder
app = wx.PySimpleApp()
userPath = 'F:/Dropbox/�����/MATLAB'
dialog = wx.DirDialog(None, "Please select your dataset folder:",defaultPath=userPath)
if dialog.ShowModal() == wx.ID_OK:
    folder_path= dialog.GetPath()
dialog.Destroy()

with open(folder_path+"\\uniqueUsers.csv") as uniUsrs:
    usrDic=[line.split(" ") for line in uniUsrs]
usrDic = dict((word, int(cnt)) for (word, cnt) in usrDic)
for filename in glob.glob(folder_path+"/*.json"):
    print(filename)
    my_file=open(filename,"r")
    read_line=my_file.readline()
    while read_line:
        json_line=json.loads(read_line)##,encoding="cp1252")#.decode("utf-8","replace")
##        if "delete" or "scrub_geo" or "limit" in json_line:
##            read_line=my_file.readline()
##            continue
        if "retweeted_status" in json_line:
            ##print(json_line["retweeted_status"]["user"]["screen_name"])
            usrDic[json_line["retweeted_status"]["user"]["screen_name"]]+=1
        read_line=my_file.readline()
    else:
        my_file.close()

my_txt = csv.writer(open("C:\\Python27\\my_python_scripts\\retweetedList.csv", "wb"))
for key, val in dict.items(usrDic):
    my_txt.writerow([key, val])
##my_txt.close()

