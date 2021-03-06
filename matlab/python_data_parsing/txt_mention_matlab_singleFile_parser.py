#-------------------------------------------------------------------------------
# Purpose:       parsing data from a txt file having a form of:
#                author1 mentioned1,mentioned2,... timestamp text \n
#                to a form:
#                author1 mentioned1 timestamp\n
#                author1 mentioned2 timestamp\n
#                thus creating a single file without the text content in order to render
#                the matlab functions more efficient.
# Required libs: wxPython GUI toolkit, python-dateutil
# Author:        konkonst
#
# Created:       31/05/2013
# Copyright:     (c) ITI (CERTH) 2013
# Licence:       <apache licence 2.0>
#-------------------------------------------------------------------------------
import os,glob
import wx
import dateutil.parser
import time

# User selects dataset folder
app = wx.PySimpleApp()
datasetPath = 'E:/konkonst/retriever/crawler_temp/'
dialog = wx.DirDialog(None, "Please select your dataset folder:",defaultPath=datasetPath)
if dialog.ShowModal() == wx.ID_OK:
    dataset_path= dialog.GetPath()
dialog.Destroy()
#User selects target folder
targetPath = 'E:/konkonst/retriever/crawler_temp/'
dialog = wx.DirDialog(None, "Please select your target folder:",defaultPath=targetPath)
if dialog.ShowModal() == wx.ID_OK:
    target_path= dialog.GetPath()
dialog.Destroy()
if dataset_path==target_path and not os.path.exists(target_path+"/new"):
    os.makedirs(target_path+"/new")
    my_txt=open(target_path+"/new/authors_mentions_time.txt","w")
elif dataset_path==target_path and os.path.exists(target_path+"/new"):
    my_txt=open(target_path+"/new/authors_mentions_time.txt","w")
else:
    my_txt=open(target_path+"/authors_mentions_time.txt","w")
#Parsing commences
for filename in glob.glob(dataset_path+"/*.txt"):
    print(filename)
    with open(filename,'r') as f:
        for line in f:
            read_line = line.strip()
            splitLine=read_line.split("\t")
            dt=dateutil.parser.parse(splitLine[2],fuzzy="True")
            mytime=int(time.mktime(dt.timetuple()))
            for mentions in splitLine[1].split(","):
                my_txt.write(splitLine[0]+"\t"+mentions+"\t"+str(mytime)+"\n") #author singlemention time
my_txt.close()
