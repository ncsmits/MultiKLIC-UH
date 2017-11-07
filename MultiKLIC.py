# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:25:09 2017

@author: Coen.Smits
"""

import pyautogui
import sys
import pymsgbox as pmb
import glob
import os
import time
from tkinter import filedialog
from tkinter import Tk

def startVIANLCS(): 
#    try: 
#        gereedschappenButton = pyautogui.locateCenterOnScreen('Tools_button.png')
#        pyautogui.PAUSE = 0.5
#        gereedschappenButton = pyautogui.locateCenterOnScreen('Tools_button.png')
#        pyautogui.PAUSE = 0.5
#        pyautogui.click(x=gereedschappenButton[0], y=gereedschappenButton[1], clicks=2, interval=0.125, button='left')
#    except: 
#        confirmBox = pmb.confirm(text='Is het Gereedschappen tabblad al geactiveerd?', title='', buttons=['Ja', 'Nee'])
#        if confirmBox == 'Nee':
#            pmb.alert('Er is iets fout gegaan', 'Fout!')
#            return
        
            
#    pyautogui.PAUSE = 1
    
    inlezenButton = pyautogui.locateCenterOnScreen('images/Inlezen_button.png')
    pyautogui.PAUSE = 0.3
    inlezenButton = pyautogui.locateCenterOnScreen('images/Inlezen_button.png')
    pyautogui.PAUSE = 0.3
    pyautogui.click(x=inlezenButton[0], y=inlezenButton[1], clicks=2, interval=0.125, button='left')
    
    pyautogui.PAUSE = 0.5
    
    browseButton = pyautogui.locateCenterOnScreen('images/Browse_button.png')
    pyautogui.PAUSE = 0.3
    browseButton = pyautogui.locateCenterOnScreen('images/Browse_button.png')
    pyautogui.PAUSE = 0.3
    pyautogui.click(x=browseButton[0], y=browseButton[1], clicks=1, button='left')
    
confirmBox = pmb.confirm(text='Zorg dat AutoCAD open is, de ViaNLCS plugin op Gereedschappen staat en deze zichtbaar is', title='', buttons=['Start','Annuleren'])
if confirmBox == 'Start':

    print("MultiKLIC gestart")
    wionFiles = []
    
    root = Tk()
    root.withdraw()
    
    wionMap = filedialog.askdirectory()
       
    for filename in glob.iglob(wionMap + '/**/*.xml', recursive=True):
        wionFiles.append(os.path.abspath(filename))
    
    print(str(len(wionFiles)) + " KLIC meldingen te verwerken.")  
      
    for i in range(0, len(wionFiles)):  
        print("\nKLIC melding " + str(i+1) + " van " + str(len(wionFiles)) + "\n" + wionFiles[i])
        startVIANLCS()      
        
        pathInput = pyautogui.locateCenterOnScreen('images/filename.png')
        pyautogui.PAUSE = 0.5
        pathInput = pyautogui.locateCenterOnScreen('images/filename.png')
        pyautogui.PAUSE = 0.5
        pyautogui.click(x=pathInput[0]+300, y=pathInput[1], clicks=1, button='left')
        
        pyautogui.typewrite(wionFiles[i] + '\n', interval=0.01)
        
        pyautogui.PAUSE = 0.5       
        gebiedCheckbox = pyautogui.locateOnScreen('images/gebied_checkbox.png')
        pyautogui.PAUSE = 0.5
        gebiedCheckbox = pyautogui.locateOnScreen('images/gebied_checkbox.png')
        pyautogui.PAUSE = 0.5 
        
        if isinstance(gebiedCheckbox, tuple):
            pyautogui.click(x=gebiedCheckbox[0]+10, y=gebiedCheckbox[1]+10, clicks=1, button='left')
        
        pyautogui.PAUSE = 0.5
        
        vetorizeButton = pyautogui.locateCenterOnScreen('images/vectorize.png')
        pyautogui.PAUSE = 0.5
        vetorizeButton = pyautogui.locateCenterOnScreen('images/vectorize.png')
        pyautogui.PAUSE = 0.5
        pyautogui.click(x=vetorizeButton[0], y=vetorizeButton[1], clicks=1, button='left')
        
        schermVIANlcs = pyautogui.locateCenterOnScreen('images/infracadscherm.png')
        
        while isinstance(schermVIANlcs, tuple):
            
            time.sleep(0.5)
            schermVIANlcs = pyautogui.locateCenterOnScreen('images/infracadscherm.png')
        
        
else:
    print("gestopt")
