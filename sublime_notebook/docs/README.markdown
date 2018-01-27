# Documentation


## Getting started

Before we proceed, here are the requirements for using this tool.

* Sublime Text
* Python 3
* [Optional] A cloud sync application setup (Dropbox, Google Drive, OneDrive etc)

So let’s begin. What you do is you first download the code from https://github.com/aviaryan/SublimeNotebook

Then you put the code files in a cloud synced or local folder of your choice. Now you are all set. You can create any number of notes in that folder. For hierarchy, you can use folders and sub-folders. Notes can be txt or md files and they will be encrypted with your password.

![How a Sublime notebook looks like](https://cdn-images-1.medium.com/max/800/1*DuTrcxf-zJ-anQShA61efw.png)

To encrypt or decrypt notes, you use the manager.py file. It runs in Python 3 and requires no additional dependencies. It is recommended you change the first line of the file to point to your interpreter.

```python
#!/Users/aviaryan/miniconda3/bin/python
```

So when you run `manager.py` for the first time, it will find the notes and ask you a password for encryption. 
After getting the password, it will encrypt all non-public notes using that password. 
In the subsequent runs, `manager.py` will work as an unlocker where it will ask password to decrypt the notes and then pause its execution. 
Now you can view and edit your notes and then later on encrypt them again by entering 'e' in the prompt.

![screen shot 2018-01-27 at 8 06 07 pm](https://user-images.githubusercontent.com/4047597/35472896-897a22a4-039d-11e8-9b1d-153c06bc203e.png)


## Note taking features

You might be wondering how does this make it a note taking application. Well, let me show you.

Open Sublime Text and click on "Open Project" in the Project menu.

Browse for the `notebook.sublime-project` file in the folder you downloaded and open it. Now open the Sidebar (View -> Sidebar). You will see all your notes presented there with the hierarchy. Whenever you want to open your Sublime Notebook, you can use the switch project shortcut (Cmd-Ctrl-P or Ctrl-Alt-P) and select notebook.sublime-project to switch to the Notebook project.

If at the moment, you are in an encrypted state, you can use Ctrl-B (Cmd-B on OSX) to launch a terminal window in the manager.py's directory. So run `manager.py` from there to decrypt your notes. Now you can update the notes in Sublime Text and re-encrypt them.

If you want to search through all your notes, use the Sublime Text’s search in project feature (Ctrl-Shift-F or Cmd-Shift-F).

If you store the folder in Dropbox or Google Drive, you can have it on all your computers. Also, I will like to add here that the Python 3 script uses no extra dependencies so you can run the script out-of-the-box on any system that has Python installed (popular Linux distros and Macs for example have it by default).


## Updating SublimeNotebook or changing password

* To update your installation of Sublime Notebook, decrypt your existing notes using old `manager.py`, then exit the script in decrypted state (using "d").
Then update the script files from this repo and start `manager.py` to re-encrypt your notes.

* Same method can be used if you want to change the password used to secure the notes.


## <a name="mdext"></a>Setup Markdown Extended for highlighting md files in Sublime Text

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


----


## FAQ

Only *.txt and *.md files are detected as notes.

You don't need to be in decrypted state to create a new note. Even when in encrypted state, you can create a note. 
When manager.py starts decrypting the notes, this new file will be ignored and will be encrypted when it's time to encrypt. 
