# Documentation

## Table of Contents

* [Requirements](#rq)
* [Getting Started](#gs)
* [Accessing your notes](#ac)
* [Encrypting your notes](#en)
* [Note taking features](#nt)
* [Changing SublimeNotebook password](#cp)
* [Customizing which folders are encrypted](#custen)
* [Setting up better Markdown highlighting in Sublime Text](#mdext)
* [FAQ](#faq)


<a name="rq"></a>
## Requirements

The requirements for using this tool are as follows. Make sure to have them installed before proceeding to the next section.

* Sublime Text
* Python 3
* [Optional] A cloud sync application setup (Dropbox, Google Drive, OneDrive etc)


<a name="gs"></a>
## Getting started

The first step is downloading the code from https://github.com/aviaryan/SublimeNotebook

Then you put the code files in a cloud synced or local folder of your choice.

Done! You can now create any number of notes in that folder. For hierarchy, you can use folders and sub-folders. Notes can be txt or md files and they will be encrypted with your password.

![How a Sublime notebook looks like](https://cdn-images-1.medium.com/max/800/1*DuTrcxf-zJ-anQShA61efw.png)


<a name="ac"></a>
## Accessing your notes

To access your notes, we will use the Projects feature of Sublime Text.

Open Sublime Text and click on "Open Project" in the Project menu.

Browse for the `notebook.sublime-project` file in the folder you downloaded and open it. Now open the Sidebar (View -> Sidebar). You will see all your notes presented there with the hierarchy. 

Whenever you want to open your Sublime Notebook, you can use the switch project shortcut (Cmd-Ctrl-P or Ctrl-Alt-P) and select `notebook.sublime-project` to switch to the Notebook project.

![Project Selector](https://user-images.githubusercontent.com/4047597/35473121-4556dd7a-03a1-11e8-8c3a-6e85592d5d5f.png)


<a name="en"></a>
## Encrypting your notes

To encrypt or decrypt notes, you use the `manager.py` file located in the notebook root. It runs in Python 3 and requires no additional dependencies. 
I recommend changing the first line of the file to point to your interpreter.

```python
#!/Users/aviaryan/miniconda3/bin/python
```

To run `manager.py`, you can use the shortcut Ctrl-B (Cmd-B on OSX) to launch a terminal window in the `manager.py`'s directory. 

Then use `python manager.py` or `./manager.py` to run the script.

When it runs for the first time, it will find the notes and ask you a password for encryption. 
After getting the password, it will encrypt all non-public notes using that password. 
In the subsequent runs, `manager.py` will work as an unlocker where it will ask password to decrypt the notes and then pause its execution. 
Now you can view and edit your notes and then later on encrypt them again by entering 'e' in the prompt.

![screen shot 2018-01-27 at 8 06 07 pm](https://user-images.githubusercontent.com/4047597/35472896-897a22a4-039d-11e8-9b1d-153c06bc203e.png)


<a name="nt"></a>
## Note taking features

If you want to search through all your notes, use the Sublime Text’s search in project feature (Ctrl-Shift-F or Cmd-Shift-F).

If you store the folder in Dropbox or Google Drive, you can have it on all your computers. Also, I will like to add here that the Python 3 script uses no extra dependencies so you can run the script out-of-the-box on any system that has Python installed (popular Linux distros and Macs for example have it by default).


<a name="cp"></a>
## Changing SublimeNotebook password

To change password of your Sublime Notebook, decrypt your existing notes using old `manager.py`, then exit the script in decrypted state (using "d").

Then start `manager.py` again to re-encrypt your notes. This time you will be asked for a new password to encrypt your notes.


<a name="custen"></a>
## Customizing which folders are encrypted

To customize which folders are encrypted, use the `settings.json` file in `sublime_notebook/` directory.

1. "private_folders" are the one that are encrypted. 
2. "public_folders" are not encrypted.

A folder by default is public if it is not included in either of them.

You can also use the "*" symbol to select all folders. For example, in the following `settings.json` file, all folders except "web_links" are private(encrypted).

```json
{
    "private_folders": [
        "*"
    ],
    "public_folders": [
        "web_links"
    ]
}
```

**NOTE** - You should edit `settings.json` file only when the notebook is in a decrypted state. Changing it when notebook is encrypted can cause 
un-intentional side-effects. `"is_encrypted": false` will be present in `settings.json` when notebook is decrypted.


<a name="mdext"></a>
## Setting up better Markdown highlighting in Sublime Text

* Install the packages from here.

	* [Sublime Markdown Extended](https://github.com/jonschlinkert/sublime-markdown-extended)
	* [Sublime Monokai Extended](https://github.com/jonschlinkert/sublime-monokai-extended) - companion to the first package.

* Make Sublime Markdown Extended as default language for markdown. 

> Navigate through the following menus in Sublime Text: View -> Syntax -> Open all with current extension as... -> Markdown Extended

* Make Sublime Monokai Extended default theme for Markdown extended. Open `Settings - Syntax Specific` from preferences and update the file as follows.

```js
{
	"color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme",
	"extensions":
	[
		"md"
	]
}
```


<a name="faq"></a>
## FAQ

Only *.txt and *.md files are detected as notes.

You don't need to be in decrypted state to create a new note. Even when in encrypted state, you can create a note. 
When manager.py starts decrypting the notes, this new file will be ignored and will be encrypted when it's time to encrypt. 
