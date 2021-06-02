# wabbajack-nexus-free-helper
Use wabbajack client with a free nexus account without loosing your mind. It will click the download buttons for you.

Due to nexus free accounts having a download limit of 2mbps it will still take you pretty much a whole day or more to download a mod pack but atleast this way you can just leave the script running on your pc while you do something else like going outside.

This project is based on [Automatic-Wabbajack](https://github.com/ge1c4t/Automatic-Wabbajack) but optimissed for speed and other benefits.

# Running the script
1. Download python and pip ( normally comes with python by default )
2. Clone this repo 
3. Have Wabbajack client running on your main display
4. In cmd or powershell run `python .\autowabbajack.pyw` 
5. The python script will use pip to install any missing modules for you, if this doesn't work you can use pip from cmd manually.
6. Make sure the Wabbajack client is visible on your monitor otherwise the script wont be able to see the buttons in the screenshot.

# Troubleshoot script always fails to find the buttons
If this happens you need to take your own screenshots of the buttons and run the script again.
Windows built in snipping tool is perfect for this.

The reason is scaling and colours can be a little bit different for each monitor so its best to create your own pngs.


