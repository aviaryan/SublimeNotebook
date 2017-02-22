# Sublime Notebook

Read this Medium post please: 


### FAQ

* Only *.txt and *.md files are detected as notes.
* You don't need to be in decrypted state to create a new note. Even when in encrypted state, you can create a note. When manager.py starts decrypting the notes, 
this new file will be ignored and will be encrypted when it's time to encrypt. 
* To update your installation of Sublime Notebook, decrypt your existing notes using old manager.py, then force exit the script before encrypting. Then update the script files from this repo and start `manager.py` to re-encrypt your notes.
* Same method can be used if you want to change the password used to secure the notes.
