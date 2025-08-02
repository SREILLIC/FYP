# FYP (Flash Your Python)  
(Work in progress since - 26 July 2025 - 5AM)  

# Intro
Choose who wins the war for your attention. Flash Your Python (before getting into your "for you page"). Syntax quiz/revision tool.  

Answering correctly launches your preferred social media platform and FYP closes.  

Disclaimer: Easy way is for android use, hard way is for WSL2 demo production.  

# Installation (the EASY way)

1 - Download ONLY the "FYP.apk" file from my GitHub repo (https://github.com/SREILLIC/FYP).  
2 - Install it on your ANDROID device.  
3 - If you don't see it, that's because apk creation failed on the last step...again.

# Installation (the HARD way - for making your own kivy apps in WSL2):  
If you didn't know, WSL2 is basically Linux installed unto Windows!  
It might help to join the discord (https://discord.gg/bootdotdev)  

Type/paste code into the CLI terminal emulator of WSL2.

## 1 - Download FYP(clone my repo) and cd into FYP dir

    git clone https://github.com/SREILLIC/FYP

## 2 - Install python3.9 and it's environment
not available by default on WSL2, so I added deadsnakes PPA(3rd-party at own risk).  
It’s a popular Ubuntu repository for installing older or alternative Python versions.  

    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update

    sudo apt install python3.9 python3.9-venv python3.9-dev

## 3 - Install global dependencies (Takes about 15 minutes at 5mbps internet speed)
    sudo apt update
    sudo apt install -y \
    git zip unzip openjdk-17-jdk python3-pip \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    zlib1g-dev libgstreamer1.0 libgstreamer1.0-dev \
    gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
    libmtdev-dev libgl1-mesa-dev libgles2-mesa-dev \
    libgstreamer-plugins-base1.0-dev libffi-dev \
    libssl-dev libsqlite3-dev libjpeg-dev libfreetype6-dev

## 4 - Setup python environment
create:  
    python3.9 -m venv .venv3_9
activate:  
    source .venv3_9/bin/activate

## 5 - Install environmental dependencies (while still in FYP dir)
(for testing your app):  
    pip install Kivy==2.3.1
    pip install pygame==2.6.1
    pip install Cython==0.29.36
    pip install pyjnius==1.5.0

## 6 - Launch (demo of app in WSL2)
Make sure android specific functions are caught with print("error") to avoid crashes.  
Example: webbrowser for opening URL vs using powershell.exe to open URL
    python3 main.py

## 7 - apk - android install file
Install buildozer:  
    pip install buildozer
Make buildozer.spec:  
    buildozer init
Configure buildozer according to how you want your apk.  
Use editor of choice (like VS code) or:  
    nano buildozer.spec
Make apk (first time can take up to an hour, depending on internet):  
    buildozer android debug

# Credits
Boot.dev back-end course for Python, Linux(WSL2), Git knowledge thus far.  

ShawCode kivy tutorials on Youtube (Useful for learning the workings of kivy - I got the updated install info for WSL2(Ubuntu) from ChatGPT).  

camera flash audio from MalarBrush @ Pixabay.  

# Some more info
## Version choices
buildozer (to make apk) only works on WSL2.  

A kivy(?) requirement called "distutils" was removed from python3.11 and onwards.  
python3.10 was not a available on deadsnakes PPA, but is theoretically compatible with kivy.  
Thus, python3.9 (latest version compatible with kivy and available on deadsnakes-PPA).  

Cython0.29.36 is latest version compatible with buildozer.  

## Personal(public)
Planning and development has been ongoing since 25 July 2025.

This is my first real coding project that I started for the bootdev hackathon 2025.  
I made a demo, submitted it for the hackathon, then rm -rf'd the ever loving orbital-nuke out of my local+GitHub folders/files, and related social media posts, because I hated how dumb my app was compared to other so-called "amateur" entries.  

A day later I realized that I'm actually doing okay'ish, considering:  
1. First month in coding.
2. First ever coding project.
3. Solo app development.
4. Kivy is kinda niche/old (I think?) and I learnt it in the same weekend.
5. Essentially did a full-stack project while only learning backend in bootdev.

So I remade the entire app and even improved functionality.   

I tried making it as easy as possible for you to install, while maintaining transparency as I'm still an unknown author.  

I used Anaconda/Jupyter notebooks for project plan to keep myself on track and partial testing of code.  

I typed most of the README while the apk was busy being made, lol(edit: while the apk was busy failing to be made - after almost an HOUR - on the last step (again) and vomiting red flavoured text errors left-right-and-center).  

Ask an AI what parts of my code does if you want to get a general idea of how it works.  

## What each global dependency does (according to ChatGPT)
Great question — understanding each of these helps you trim fat and only install what you actually need for your use case (especially if you're not dealing with media-heavy apps). Here's a clean breakdown of what each package does:  

🔧 Core Tools  
Package	Purpose  
git	Used by Buildozer to fetch recipes or dependencies from GitHub  
zip, unzip	Used for compressing and extracting archives during build  
openjdk-17-jdk	Required for compiling Java code into an Android APK  
python3-pip	Needed to install Python packages via pip  

🕹️ SDL2-related (Kivy’s windowing/input/audio backend)  
Package	Purpose  
libsdl2-dev	Core SDL2 dev headers — required for rendering/input in Kivy  
libsdl2-image-dev	Adds image format support (PNG, JPEG, etc.)  
libsdl2-mixer-dev	Adds sound format support (WAV, MP3, OGG, etc.)  
libsdl2-ttf-dev	Adds TrueType font rendering support  

If you're not using images, sound, or custom fonts, some of these may be optional — but they're safe defaults for general Kivy apps.  

🎹 Multimedia (Video/audio playback)  
Package	Purpose  
libportmidi-dev	Enables MIDI support (used by some music/audio apps)  
libswscale-dev, libavformat-dev, libavcodec-dev	Required for video/audio processing (part of ffmpeg)  

If you don’t use video/audio/media streaming, these can be skipped.  

🗜️ Compression & File Handling  
Package	Purpose  
zlib1g-dev	Adds support for compressed data handling (used in various places)  
libffi-dev	Needed for calling C functions from Python (used by CFFI, PyJnius, etc.)  
libssl-dev	Required for HTTPS connections (requests, etc.)  

🎥 GStreamer (advanced audio/video playback)  
Package	Purpose  
gstreamer1.0-plugins-base	Basic GStreamer plugins (used by Kivy for video/audio)  
gstreamer1.0-plugins-good	Recommended safe plugins  
gstreamer1.0-plugins-bad, gstreamer1.0-plugins-ugly	Adds extra codec support (some may have licensing concerns)  
libgstreamer-plugins-base1.0-dev	GStreamer development headers for building against  

Skip if you're not playing video or audio streams.  

🎨 Input, Rendering, Fonts, and Images  
Package	Purpose  
libmtdev-dev	Enables multitouch input (for mobile/touch devices)  
libgl1-mesa-dev, libgles2-mesa-dev	Provide OpenGL ES support for rendering (used by Kivy)  
libsqlite3-dev	Needed if you use SQLite database in your app  
libjpeg-dev	For JPEG image support (used by Pillow)  
libfreetype6-dev	For font rendering support (used by Pillow, Kivy, etc.)  