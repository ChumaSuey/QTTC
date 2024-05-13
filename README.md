# QTTC (Quake Trigger Text Converter)

For a while i've been doing manually all my text input into Quake via Trenchbroom, using Word and notepad to make small quick notes.
I decided to make a small script to automate the process, and of course, have fun in the journey (with the help of my friend Nepta in coding).
While mappers may just do it on their own manually and naturally i decided to make a small python script to help me, and maybe others.

## How to run it and what does is it require?

The script requires Python installed in your machine, it was interpreted or made with Python 3.9, but a regular python version should be enough for the script to work.

In the case the script doesn't work for some reason and you wanna try out installing the libraries and modules manually, the ones used are:
- TKInter.
- Pyperclip.

Works in Windows 11, 10 and in Linux it has been tested in Mint and Arch with a python version. (hope it runs for you as well)

QTTC-Win is the windows version, QTTC-Linux is the linux version (binaries made in Ubuntu)

## Instructions on how to use the script (from the GUI perspective) with direct steps.

from Wadcleaver GUI's feedback i've implemented and Nepta did an optimization so it looks good in most screens, but here it is what you will see.

1. Open the script

![image](https://github.com/ChumaSuey/QTTC/assets/3680154/621a7b42-3e84-431b-b358-13f4a3446a7e)

2. Input the text into the text input field.

So we will use an extract from the song "The root of all evil" by Dream Theater with some adds to make an example:

Proud "enough" for you to call me arrogant
Greedy 'enough' to be labeled a thief
Angry enough for me to go and hurt a man
Cruel enough for me to feel no grief

this will be our input.

3. Click preview to verify the text.

![image](https://github.com/ChumaSuey/QTTC/assets/3680154/7602a40a-e9fd-4f3d-9536-fd9a9262a983)

Here we see the 3 functions the script does:
- It line breaks the line at 40 chars maximum.
- Converts " " into `
- Converts ' into `  (this one was a test case thought by me since i use word for writing the text)

4. Choose your method of saving the text.

"Copy" button will extract the text and copy/paste it wrapped up:
> Proud `enough` for you to call me\narrogant Greedy `enough` to be labeled a\nthief Angry enough for me to go and hurt\na man Cruel enough for me to feel no\ngrief

"Save as TXT File" will just save the text as a text file wherever you point the path at (in Windows it's a typical save, indicate name of the file and where you want it saved with the explorer)

## Notes

The program / script has been tested and worked so far, it'd be ok to always check the char amount and if any other typos the Quake engine doesn't like... It's mean't to automate or aid in the process of those mappers that wanna make a story densed map for any mod, or just to make sure the text can be used in Quake as messages in the respective message field for some entities.

It's expected the user writes in english, we covered basic limitations the Quake engine may not like in text, but that's it... maybe until some other time we can add more.

I had an issue when creating the binaries with Windows, i think i solved it with just including Pyperclip as a "hidden" or special import, while Linux version doesn't have this, it works... so yeah! just a small curiosity.

The linebreak or "go to the next line" is implicit in the visual preview, but it works when creating the txt file or copying the text from the converter, just a small note.

## Backend or Behind the scenes.

There are 2 py files, GUI and Main.

GUI is basically TKInter doing it's job on the front to make sure the buttons, printing and file management work.

main.py is the pure backend, using textwrap and basic outline commands Python will make sure the 3 limitations imposed in text work correctly.

There is a py file that does it on Python Console but it's outdated and that was just a left over from experimentation.

## Credits and Special thanks.

Programmers:
- Chuma.
- Nepta.
co crediting my small freelance development team:
- Absolute Quantum (AQ) [special mention to my friend Dany]

Special thanks.
- Mikolah (textwrapper suggestion, ty bro)
- 4LT (Linux Arch testing)
- Admer (Linux Mint testing)
- CommonCold (Windows 10 testing)
- Riktoi (Windows 11 testing)
- R639 and Borizilla for looking and giving small feedback to our script.



