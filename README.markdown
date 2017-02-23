# Sublime Notebook

**Read the Medium post for setup instructions**:
https://medium.com/aviaryan/sublime-notebook-an-attempt-to-use-sublime-text-as-my-note-taking-application-b8d846c47905#.hy8alq2ip


## Features

* Search across all notes
* Hierarchical organization and display of notes
* Password based encryption
* Cloud sync
* Markdown based markup and syntax highlighting


## FAQ

* Only *.txt and *.md files are detected as notes.
* You don't need to be in decrypted state to create a new note. Even when in encrypted state, you can create a note. When manager.py starts decrypting the notes, 
this new file will be ignored and will be encrypted when it's time to encrypt. 
* To update your installation of Sublime Notebook, decrypt your existing notes using old manager.py, then force exit the script before encrypting. Then update the script files from this repo and start `manager.py` to re-encrypt your notes.
* Same method can be used if you want to change the password used to secure the notes.


## <a name="mdext"></a>Setup Markdown Extended for highlighting md files

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
