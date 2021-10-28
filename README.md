# README

This code is compatible with both Ubuntu and Raspbian. See line 33-37 in main.py <br>

    # this command confimred to work for Raspbian
    command = "pcmanfm --set-wallpaper " + file
    # this command confimred to work for Ubuntu
    command = "gsettings set org.gnome.desktop.background picture-uri '" + file + "'" 
    

for this script to run on each boot, add below line in your crontab. <br>

``` 
@reboot <path to script>/main.py
```
