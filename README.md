# Transfer Models from World of Warcraft to Tabletop Simulator

## Introduction
Using already existing, textured, and posed 3D models is a quick way to save time when looking for visual representations of objects in Tabletop Simulator. One great source of such models, that can be downloaded, but not redistributed, for free is World of Warcraft. These steps will walk you through setting up scripts to import assets from World of Warcraft into Tabletop Simulator. This will allow you to quickly and easily add assets of your choice into Tabletop Simulator. These steps may take a while, but in the long run will allow you to save time. 

## Terms to know
 - **Path** - the location of a folder or file on your computer. For example C://CustomTTS/minis/temp is located in the minis folder, which is in the CustomTTS folder, which is located on drive C://

## Software List
 * [AutoHotkey 1.1](https://autohotkey.com/download/ "Download AutoHotkey")
 * [Blender 2.78c](https://www.blender.org/download/ "Download Blender") 
 * [Tabletop Simulator v10.3](https://store.steampowered.com/app/286160/Tabletop_Simulator/ "Tabletop Simulator Steam Page")
 * [PILLOW 5.4.1](https://pillow.readthedocs.io/en/stable/ "Pillow Documentation")
 * [Python 3.7.2](https://www.python.org/downloads/ "Download Python")
 * [Windows 10 Operating System](https://www.microsoft.com/en-us/store/b/windows?activetab=tab%3ashopwindows10 "Download Windows 10")
 * [World of Warcraft 8.1.5](https://worldofwarcraft.com/en-us/ "Download World of Warcraft")
 * [WoW Model Viewer 0.9.0.beta13](https://wowmodelviewer.net/new/download/ "Download WoW Model Viewer")
 
> **Notice:**  *Instructions are for exact software versions specified. Results may vary in other software version*
 

## Directions

### Install Software Prerequisites

When installing software prerequisites you need to be careful to make sure the versions match those described in the software list. Other versions of software may not work as intended.

You cannot download old versions of World of Warcraft. You will have to download the latest version. Versions of WoW Model Viewer correspond to versions of World of Warcraft, so you will have to download the latest version of WoW Model Viewer as well. 

It is recommended you install all of these programs to default directories with default settings.

### Download Additional Files

You will have to [download the CustomTTS folder from here](https://drive.google.com/file/d/1xaXMOU7zcclb0x2SJZ7X5PzReMS319U5/view?usp=sharing "Download CustomTTS From Google Drive"). This is the folder that contains all of the scripts we will be using.

### Extract the Files

1. You will need to extract the .zip folder. To do so, you will need to go to your downloads folder. This process varies by browser. In Firefox there is an icon of a downward facing arrow above a horizontal line in the top-right corner. Click that icon and, from the dropdown, next to CustomTTS.zip, click the black and white folder icon.

2. Once you are in your downloads folder, right-click on "CustomTTS.zip" and then select "Extract All...". A pop-up will appear that asks you to "Select a Destination and Extract Files". You should see a text box.

   Type into the textbox the directory where you want CustomTTS to end up. I recommend "C:\CustomTTS". Make sure the box labeled "Show extracted files when complete" is checked, then click "Extract". After this point you will not need CustomTTS.zip, and it can be safely deleted.

![Make sure the extration path is "C:\CustomTTS and the "Show extracted files when complete" box is checked.](https://i.imgur.com/Cqv0cmP.png)

3. There may be a brief pause, and then a new window should pop-up showing two folders named "minis" and "scripts". This is the inside of the CustomTTS folder. It is in this folder that all scripts and files will be located. We will spend the next few steps navigating through this folder. 

![The folders should be named "minis" and "scripts"](https://i.imgur.com/wHzR0yM.png)

### Open Blender, WoW Model Viewer, and Scripts

1. In the two folders that just appeared, navigate to "minis", then "meta", then double click on "emptyunifyscript.blend". A .blend file is a type of file that Blender uses to save a scene. "emptyunifyscript.blend" has a specific list of presets to work better with our models. Be careful not to save over this file within blender.

![Make sure you're clicking on "emptyunifyscript.blend"](https://i.imgur.com/pWLTDGq.png)

2. In the explorer navigate back to the CustomTTS main folder. You should see "minis" and "scripts" again. This time go to "scripts", then "minis", then "wow_to_TTS". Then double click on wow2TTS.ahk. This is an AutoHotkey script. It is what will handle all of the various input that you'd normally need to enter by hand.

3. You will also need to open WoW Model Viewer and load World of Warcraft. This may take quite some time. Please avoid clicking on the WoW Model Viewer window during this time, as it will cause Windows to realize it isn't responding. Windows may then force it to close before loading World of Warcraft is complete.

### Exporting into Blender

4. In WoW Model Viewer open a model you want to export into blender.

5. Press windows key and the "z" key at the same time. Do not press any other buttons, and wait until the script finishes running. You will know the script is finished when it has switched your view over to blender and the cursor has returned to normal.

![An example of a posed model in WoW Model Viewer.](https://i.imgur.com/ZSjpdJY.png)

6. The model has now been imported into blender. You are free to perform any changes to the model, but do not overwrite the .blend file. Instead go to "file" and "export" to "output_clean.obj" in the CustomTTS/minis/temp folder.

![That same model in Blender.](https://i.imgur.com/17sgfge.png)


### Importing into Tabletop Simulator

1. To import the model into Tabletop Simulator, open Tabletop Simulator, and open the game where you want to import the model. 

2. Then, go to "Objects", "Components", "Custom" and "Model". A pop-up should then appear. For the "Model/Mesh" field click to yellow folder icon to its right, and then navigate to your CustomTTS folder. Then go to "minis", "temp" and "output_clean.obj".

3. Tabletop Simulator will then ask if you want to upload this item to the cloud. Select the "local" option. A file path should appear in the text field. If you examine it closely it should be the full path to the the "output_clean.obj" file.

4. For the "Diffuse/Image" field repeat this process, except you will be selecting "one.png" instead of "output_clean.obj". Again, you will want to select the "local" option.

![What the "Model" tab should look like when you are done.](https://i.imgur.com/MUOknw8.png)

5. Switch over to the "Material" tab and select the "Cardboard" preset at the top. Then, click "import".

![What the "Material" tab should look like when you are done.](https://i.imgur.com/ll2lUK3.png)

If everything went well, then you're done.

![What the finished product should look like.](https://i.imgur.com/H8l4cBa.png)
