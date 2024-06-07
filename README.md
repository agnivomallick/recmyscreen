# recmyscreen

RecMyScreen is a free to use screen recorder.

Features:

- Play, Pause, Resume, Stop recording
- Saving in mp4 (I am seeing how to save in a wide variety of formats)

## Installation

That's just easy. Download the `exe` file from the [Releases](https://github.com/agnivomallick/recmyscreen/releases/)

## Build from source

You can also do build from source by following the steps.

- Clone the repository using `git clone` and then the URL in Code > the URL
- **IT IS RECOMMENDED TO CREATE A VIRTUAL ENVIRONMENT**.
- However you **can** run in a normal environment.
- Install the packages using `pip install -r requirements.txt`. Make sure to navigate to the directory where you cloned it.
- Please adhere to the [MIT License](https://github.com/agnivomallick/recmyscreen/blob/main/LICENSE)
- But I strongly recommend to NOT edit the resources/ directory as it contains the resources and a resource file that helps to import them from the app. If you edit it cannot import the resources and as a result you will have a no-graphics like app.
- Then you can build your exe.
- You can use pyinstaller, cx-freeze, or anything you want. This part (from now) I am not mentioning.
- Then you can package it as a setup file and distribute.

## Tools and Editors used

For editing code, I used Microsoft Visual Studio 2022.

For the app, I used Qt 6.7 for GUI, pyscreenrec for Screen Recording.

There are also ctypes and os package. You can see the comments in the file.

## Licensing

This product is licensed under the terms of the [MIT License](https://github.com/agnivomallick/recmyscreen/blob/main/LICENSE).
