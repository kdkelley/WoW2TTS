#CommentFlag //

//Paste customTTS's path after the equal sign (leave a space between the equal sign and the path)
customTTSPath = 

func_cleartemp()
{
global customTTSPath
RunWait % customTTSPath . "\scripts\minis\wow_to_TTS\cleartemp.bat"
}

func_genchardata()
{
global customTTSPath
RunWait % customTTSPath . "\scripts\minis\wow_to_TTS\getchardata.bat"
}

func_focuswowmv()
{
WinWait ahk_exe wowmodelviewer.exe
WinActivate ahk_exe wowmodelviewer.exe
WinWaitActive ahk_exe wowmodelviewer.exe
Sleep, 500
}

func_importwowmv()
{
global customTTSPath
Send, {F8}
Sleep, 4000
Send, {Tab 5}
Send, {Enter}
Send, % customTTSPath . "\scripts\minis\wow_model_viewer_changer"
Send, {Enter}
Send, {Tab 6}
Sleep, 7000
Send, output.chr
Send, {Enter}
Sleep, 20000
}

func_disableeyeglow()
{
Send, {Alt}
Sleep, 1000
Send, {Right 2}
Sleep, 500
Send, {Down 4}
Sleep, 500
Send, {Right}
Sleep, 500
Send, {Enter}
Sleep, 500
}

func_exportwowmv()
{
global customTTSPath
Send, {Alt}
Sleep, 1000
Send, {Down 7}
Sleep, 500
Send, {Right}
Sleep, 500
Send, {Down 2}
Sleep, 500
Send, {Enter}
Sleep, 5000
Send, {Tab 6}
Send, {Enter}
Send, % customTTSPath . "\minis\temp"
Sleep, 1000
Send, {Enter}
Sleep, 1000

Send, !n
//Send, {Tab 1}
//Sleep, 100
//Send, {Tab 1}
//Sleep, 100
//Send, {Tab 1}
//Sleep, 100
//Send, {Tab 1}
//Sleep, 1000
//Send, {Tab 1}
//Sleep, 1000
//Send, {Tab 1}
//Sleep, 1000

Sleep, 3000
Send, output.obj
Send, {Enter}
Send, +{Tab}
Send, {Enter}
Sleep, 3000
Send, {Enter}
}

func_quickexportwowmv()
{
Send, {Alt}
Sleep, 500
Send, {Down 7}
Sleep, 500
Send, {Right}
Sleep, 500
Send, {Down 2}
Sleep, 500
Send, {Enter}
Sleep, 500
Send, output
Sleep, 1000
Send, {Enter}
Sleep, 1000
Send, {Enter}
}

func_combinetextures()
{
global customTTSPath
RunWait % customTTSPath . "\scripts\minis\wow_to_TTS\makeonetexture.bat"
}

func_focusblender()
{
WinWait ahk_exe blender.exe
WinActivate ahk_exe blender.exe
WinWaitActive ahk_exe blender.exe
}

func_loadblend()
{
MouseMove, 350, 350, 0
Send, ^+o
Click
}

func_runblendscript()
{
MouseMove, 1100, 200, 0
Send, !p
}

func_postgen()
{
func_focuswowmv()
// func_disableeyeglow()
func_exportwowmv()
func_combinetextures()
func_focusblender()
func_loadblend()
func_runblendscript()
}

#n::
func_genchardata()
func_focuswowmv()
func_importwowmv()
func_postgen()
return

#z::
func_postgen()
return

^e::
func_cleartemp()
func_quickexportwowmv()
func_combinetextures()
func_focusblender()
func_loadblend()
func_runblendscript()
return