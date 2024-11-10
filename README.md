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

QTTC-Win is the windows version, QTTC-Lin is the linux version (binaries made in Ubuntu)

## Instructions on how to use the script (from the GUI perspective) with direct steps.

from Wadcleaver GUI's feedback i've implemented and Nepta did an optimization so it looks good in most screens, but here it is what you will see.

We've made some changes to the script in order to have more functions, so pictures are rather different than the previous version:

1. Open the script

![image](https://github.com/user-attachments/assets/1c2254ca-6009-4cef-9b01-68e2ba92298c)


2. Input the text into the text input field.

![image](https://github.com/user-attachments/assets/6775492e-0fdd-4495-993d-fa0a8a434b54)

So we will use an extract from the song "The root of all evil" by Dream Theater with some adds to make an example:

Proud "enough" for you to call me arrogant
Greedy 'enough' to be labeled a thief
Angry enough for me to go and hurt a man
Cruel enough for me to feel no grief

this will be our input.

3. Click Translate to verify the text.

![image](https://github.com/user-attachments/assets/64cf7ec2-7d07-46c5-b9a4-21135320d31b)

Here we see the 3 functions the script does:
- It line breaks the line at 40 chars maximum.
- Converts " " into `
- Converts ' into `  (this one was a test case thought by me since i use word for writing the text)

The text appears as if it would be inserted into Trenchbroom, this change remains intentional because basically this text is the variable the script is saving to keep the text.

4. Choose your method of saving the text.

This part was reworked on to have more options at hand.

![image](https://github.com/user-attachments/assets/a1c2174c-e887-4554-b178-0e9e6b22eb51)




"Copy" button will copy the text into clipboard:
> Proud `enough` for you to call me\narrogant Greedy `enough` to be labeled a\nthief Angry enough for me to go and hurt\na man Cruel enough for me to feel no\ngrief

"Copy into trigger_relay" will copy the text into clipboard (intended to be copied into Trenchbroom) as a trigger_relay filling the "message" field, this was made to copy it as a reference to a point entity.

"Copy into trigger_textstory" will copy the text into clipboard (intended to be copied into Trenchbroom) as a trigger_textstory filling the "message" field ( a brush of 3 units of height and wide), this was made to copy it as a reference to a brush entity.

With this, the main functionality is covered, so the other 3 buttons that remain are the following ones :

"Save" will just save the text as a text file wherever you point the path at (in Windows it's a typical save, indicate name of the file and where you want it saved with the explorer)

"Clear" will clear the input and output text.

This one is a bit more complex but i'll explain quickly:

"Linebreak Cleaning" will just clean the existent text of any linebreak "/n" within the text input field, this was programmed so the mapper doesn't have to get to the original notes to retranslate the desired text.

So in the example the translated text : 
> Proud `enough` for you to call me\narrogant Greedy `enough` to be labeled a\nthief Angry enough for me to go and hurt\na man Cruel enough for me to feel no\ngrief

When the button is pressed it, the text results in:
> Proud `enough` for you to call me arrogant Greedy `enough` to be labeled a thief Angry enough for me to go and hurt a man Cruel enough for me to feel no grief

A couple of images so the button functionality can be visualized:

![image](https://github.com/user-attachments/assets/6fb7b2f4-0a1c-4615-bef1-817b3945477d)

![image](https://github.com/user-attachments/assets/37c863e4-6a16-477d-94d7-0157170cef5e)

As it can be seen within the green lines in the text input field, the linebreaks have been cleaned... the red lines are where the linebreaks should go.


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

As of version V2.5 what has been implemented is that the Clear button cleans both input and output.

The Copy into Trigger_textstory and Copy into Trigger_relay will just print text with the translated variable inside, so it's copied into the clipboard with the intention to be copied to Trenchbroom (it works)

## Credits and Special thanks.

Programmers:
- Chuma.
- Nepta.
co crediting my small freelance development team:
- Absolute Quantum (AQ) [special mention to my friend Dany]

Special thanks.
- Mikolah (textwrapper suggestion, ty bro)
- 4LT (Linux Arch testing and also feedbacks and observation to improve the script)
- Admer (Linux Mint testing)
- CommonCold (Windows 10 testing)
- Phoenyx (Windows 10 testing)
- Rabbit (Windows 11 and Mint testing)
- 66ppt99 (Windows 11 testing)
- Riktoi (Windows 11 testing)
- R639 and Borizilla for looking and giving small feedback to our script.



