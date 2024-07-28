# RofloSvin

RofloSvin is a free and open source bot for Discord made with discord.py. You can run it on your computer or in the cloud. The bot is safe because you control its code yourself.

![Svin Doc](img/svin-doc.jpg)

## Features:

This bot has been in development since 2024. Here is everything the command bot can do:

## Games features

- `$start` - this command is used for a text game in the basic EN language
- `$start ru` - this command is used for a text game in RU language
- `$continue [1] or [2]` - this command is used to continue the game
- `$start shooter` - this command used for begin Shooter game
- `$attack` - this command used for attack enemy in shooter game
- `$dodge` - with this command you will dodge or maybe not enemy attack
- `$use_potion` - with this command you use a health potion
- `$flip` - command to play Heads&Tails

## Music features

- `$p [youtube url]` - command to play music in the voice channel
- `$s` - command to stop the music
- `$n` - command to play next song in queued
- `$l` - command еo make the bot leave the voice channel

## Help commands

- `$help` - this command tells basic information about the bot, prefix and commands.
- `$help_info` - this command explains in detail about our bot, which commands are important, etc.


# Instalation

This bot is developed on python you will need atleast 3.8. In order for music playback to work you will need ffmpeg.

## Windows

1. Install [python](https://www.python.org/downloads/)
2. Install [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/download)
3. Install [ffmpeg](https://www.ffmpeg.org/download.html)

For ffmpeg you will need

1. Click on the link and select the Windows version of FFmpeg.
2. Download and unzip the archive to a convenient location, for example, C:\ffmpeg.
3. Add the path to the bin folder inside the unpacked FFmpeg directory to your system environment variables:

After that you will need to do run cmd as admin and type this command `setx /m PATH “C:\ffmpeg\bin;%PATH%”`
if you are successful, restart your computer and check if everything is ok with ffmpeg and write the command `ffmpeg -version`


### Additional Resources

- [Instaling python for windows](https://docs.python.org/3/using/windows.html)
- [Instaling ffmpeg for windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)



Now your project is ready to run. You can work with the project in the IDE of your choice.



PROVIDE BY [cyweee](https://github.com/cyweee), [korvander](https://github.com/KoRvAndeR), [artimok1](https://github.com/Artimok1)

