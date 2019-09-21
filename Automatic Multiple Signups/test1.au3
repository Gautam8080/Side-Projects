#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_UseX64=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#include <MsgBoxConstants.au3>
#include <IE.au3>
#include <Constants.au3>
#include <array.au3>
#include <file.au3>
Local $i = 1
Local $file = FileOpen(@scriptdir & "\emailinlinenew.txt", 0)
If $file = -1 Then
MsgBox(0, "Error", "Unable to open file.")
Exit
EndIf
Local $answer = InputBox("AutoSign-Up", "Enter number of signups", "")
While $i < ($answer*4)
	$line = FileReadLine($file, $i)
	$name = FileReadLine($file, $i+1)
	$last = FileReadLine($file, $i+2)
	$pass = FileReadLine($file, $i+3)
	ConsoleWrite($line & @CRLF)
	If @error Then ExitLoop ;
	ShellExecute ("C:\Users\Gautam\Desktop\CS\TOR\Tor Browser\Browser\firefox", "https://app.reviewr.com/s1/pitch?subid=4474895&evtid=4281505")
	Sleep(Random(20000, 25000, 1))
	MouseClick("left", 850, 250) ; click for login
	;sleep(3000)
	MouseClick("left", 1130, 330) ; create acc
	;sleep(1000)
	MouseClick("left", 1017, 437) ; email
	ControlSend("[ACTIVE]", "", "", $line)
	;Send($line)
	sleep(0)
	MouseClick("left", 1022, 519) ; first name
	Send($name)
	sleep(0)
	MouseClick("left", 1022, 600) ; last name
	Send($last)
	sleep(0)
	MouseClick("left", 1022, 700) ; pass
	Send($pass)
	sleep(0)
	MouseClick("left", 1033, 733) ; scroll down
	Send("{DOWN}")
	Send("{DOWN}")
	sleep(0)
	MouseClick("left", 1033, 669) ; pass again
	Send($pass)
	Sleep(0)
	MouseClick("left", 1033, 733) ; submit
	sleep(15000)
	MouseClick("left", 845, 257) ;like button
	Sleep(1000)
	MouseClick("left", 845, 257)
	Sleep(8000)
	WinClose("[ACTIVE]")
	$i = $i + 4
WEnd
FileClose($file)
