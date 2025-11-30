; -------------------------------
; Brliant Calculator v2.1.2 Installer
; -------------------------------

!include "MUI2.nsh"
!include "nsDialogs.nsh"
!include "LogicLib.nsh"
!include "WinMessages.nsh"
!include "FileFunc.nsh"
!include "StrFunc.nsh"

; Initialize String Functions
${StrStr}
${StrRep}
${UnStrRep}

Name "Brliant Calculator v2.1.2"
OutFile "Brliant_Calc_Installer.exe"
InstallDir "$PROGRAMFILES\Brliant Calculator"
RequestExecutionLevel admin
ShowInstDetails show
ShowUninstDetails show

!define DEFAULT_CMDNAME "brliant_calc"
!define VERSION "2.1.2"

Var CMDNAME
Var CMDLABEL

; -----------------------
; Initialization
; -----------------------
Function .onInit
  StrCpy $CMDNAME "${DEFAULT_CMDNAME}"
FunctionEnd

; -----------------------
; Pages
; -----------------------
!insertmacro MUI_PAGE_WELCOME
Page custom SelectNamePage SelectNameLeave
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

; -----------------------
; Custom Page – Command Name
; -----------------------
Function SelectNamePage
  nsDialogs::Create 1018
  Pop $0
  ${If} $0 == error
    Abort
  ${EndIf}

  ${NSD_CreateLabel} 0u 10u 100% 12u "Choose the command name (no extension)"
  Pop $0

  ${NSD_CreateText} 0u 30u 100% 12u "$CMDNAME"
  Pop $CMDLABEL

  ${NSD_CreateLabel} 0u 48u 100% 40u "This will be the command you type in the terminal (e.g., 'brliant_calc').$\n$\nNEW in v2.1.0: You can also create custom aliases after installation using:$\n  sudo brliant_calc -changeCall <alias_name>"
  Pop $0

  nsDialogs::Show
FunctionEnd

Function SelectNameLeave
  ${NSD_GetText} $CMDLABEL $CMDNAME

  ; Remove .exe if user typed it
  ${StrStr} $0 $CMDNAME ".exe"
  ${If} $0 != ""
    ${StrRep} $CMDNAME "$CMDNAME" ".exe" ""
  ${EndIf}

  ; If empty → fallback
  StrCmp $CMDNAME "" 0 +2
    StrCpy $CMDNAME "${DEFAULT_CMDNAME}"
FunctionEnd



; =========================
; INSTALL
; =========================
Section "Install"

  SetOutPath "$INSTDIR"
  CreateDirectory "$INSTDIR"

  ; Copy program
  ; IMPORTANT: Build the exe first using PyInstaller:
  ;   pyinstaller --onefile brliant_calc\__main__.py -n brliant_calc
  ; The exe will be in dist\brliant_calc.exe
  File /oname=brliant_calc.exe "brliant_calc.exe"

  ; Rename to chosen command name
  StrCpy $R0 "$INSTDIR\$CMDNAME.exe"
  Rename "$INSTDIR\brliant_calc.exe" "$R0"

  ; Create .bat wrapper for compatibility
  StrCpy $R1 "$INSTDIR\$CMDNAME.bat"
  FileOpen $2 "$R1" w
  FileWrite $2 '@"%~dp0\$CMDNAME.exe" %*$\r$\n'
  FileClose $2

  ; Start Menu shortcut
  CreateDirectory "$SMPROGRAMS\Brliant Calculator"
  CreateShortCut "$SMPROGRAMS\Brliant Calculator\Brliant Calculator.lnk" "$R0"

  ; Write uninstall program
  WriteUninstaller "$INSTDIR\Uninstall.exe"

  ; Add uninstall registry entries
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Brliant Calculator" "DisplayName" "Brliant Calculator v${VERSION}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Brliant Calculator" "UninstallString" "$INSTDIR\Uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Brliant Calculator" "DisplayIcon" "$R0"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Brliant Calculator" "DisplayVersion" "${VERSION}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Brliant Calculator" "Publisher" "Aarav Maloo"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Brliant Calculator" "URLInfoAbout" "https://github.com/aaravmaloo/brliant_calc"

  ; Add to PATH if missing (User Path)
  ReadRegStr $3 HKCU "Environment" "Path"
  
  ; Check if INSTDIR is already in PATH
  ${StrStr} $0 $3 "$INSTDIR"
  ${If} $0 == ""
    StrCpy $3 "$3;$INSTDIR"
    WriteRegExpandStr HKCU "Environment" "Path" "$3"
    System::Call 'User32::SendMessageTimeoutA(i 0xffff, i ${WM_SETTINGCHANGE}, i 0, t "Environment", i 0x0002, i 500, *i .r0)'
  ${EndIf}

  ; Store install info for uninstaller
  WriteRegStr HKLM "SOFTWARE\BrliantCalculator" "CmdName" "$CMDNAME"
  WriteRegStr HKLM "SOFTWARE\BrliantCalculator" "InstallDir" "$INSTDIR"
  WriteRegStr HKLM "SOFTWARE\BrliantCalculator" "Version" "${VERSION}"

  ; Show completion message with new features
  MessageBox MB_OK "Brliant Calculator v${VERSION} installed successfully!$\n$\nCommand: $CMDNAME$\n$\nNEW: Create custom aliases with:$\n  sudo $CMDNAME -changeCall <alias>$\n$\nExample: sudo $CMDNAME -changeCall bcalc"

SectionEnd



; =========================
; UNINSTALL
; =========================
Section "Uninstall"

  ReadRegStr $1 HKLM "SOFTWARE\BrliantCalculator" "InstallDir"
  StrCmp $1 "" 0 +2
    StrCpy $1 "$PROGRAMFILES\Brliant Calculator"

  ReadRegStr $CMDNAME HKLM "SOFTWARE\BrliantCalculator" "CmdName"

  ; Remove files
  Delete "$1\$CMDNAME.exe"
  Delete "$1\$CMDNAME.bat"
  Delete "$1\Uninstall.exe"

  Delete "$SMPROGRAMS\Brliant Calculator\Brliant Calculator.lnk"
  RMDir "$SMPROGRAMS\Brliant Calculator"

  ; Ask about removing custom aliases and config
  MessageBox MB_YESNO "Do you want to remove custom aliases and configuration files?" IDYES RemoveConfig IDNO SkipConfig
  RemoveConfig:
    RMDir /r "$APPDATA\brliant_calc"
    RMDir /r "$USERPROFILE\.brliant_calc"
  SkipConfig:

  ; Remove registry keys
  DeleteRegKey HKLM "SOFTWARE\BrliantCalculator"
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Brliant Calculator"

  ; Fix PATH (User Path)
  ReadRegStr $3 HKCU "Environment" "Path"
  
  ; Remove path entry
  ${UnStrRep} $3 "$3" ";$1" ""
  ${UnStrRep} $3 "$3" "$1;" ""
  ${UnStrRep} $3 "$3" "$1" ""
  
  WriteRegExpandStr HKCU "Environment" "Path" "$3"
  System::Call 'User32::SendMessageTimeoutA(i 0xffff, i ${WM_SETTINGCHANGE}, i 0, t "Environment", i 0x0002, i 500, *i .r0)'

  ; Remove install directory
  RMDir "$1"

SectionEnd