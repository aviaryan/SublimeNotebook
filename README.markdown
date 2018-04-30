<h1 align="center">
	Sublime Notebook :memo:
</h1> 

**v2.1**

Sublime Notebook is an attempt to use Sublime Text as a complete note taking application.

> Blog post for v0.3.0 (no longer recommended) https://medium.com/aviaryan/b8d846c47905#.hy8alq2ip


## Why did you build this? :thinking:

I have been note-taking for as long as I started using computers. I use notes mostly for technical stuff, but these days I am using notes to record all kinds of information like journals, ideas, snippets etc. In my career, I have tried a number of note-taking tools like OneNote, Evernote, CintaNotes, SimpleNote, Cherrytree, Google Keep, etc. But I have never been satisfied with them mainly because - 

1. I don't have any control over how or where my notes are stored. - What if the company closes or the developer stops building the product?
2. Most of these services are paid or work on only certain Operating Systems. And even if they are truly free and cross-platform, they lack critical features like fast full notebook search or hierarchical organization.

Because of these reasons, I had to lose my notes a number of times and was forced to start from scratch. This was frustrating, and finally, I decided to do something about it.

The result is this project, a wrapper/idea that converts my favorite text editor, Sublime Text, to a feature-rich note-taking tool. Sure it might not be as polished as all those premium note-taking tools, but it works and that too in the way I want it to. And if for some reason I get tired of using Sublime Text, I can just port this to any other text editor like VSCode. It will be easy because the dependency on the text editor is very minimal here, not to mention the notes are nothing but plain text files. 😉


## Features :sunglasses:

* Faaaast Search across all notes (thanks to Sublime Text)
* Hierarchical organization and display of notes
* Password based encryption for notes (thanks to [pyAES](https://github.com/ricmoo/pyaes))
* Cloud sync (Dropbox, Google Drive, Box, etc)
* Periodic git backup (to Github, Gitlab, your own private git server, etc)
* Markdown based markup and code syntax highlighting


## Documentation :yum:

Find the docs in the [sublime_notebook/docs](sublime_notebook/docs/README.markdown) folder.


## Ports :left_right_arrow:

[VSCode Notebook](https://github.com/aviaryan/VSCodeNotebook) - A spin-off of this project that works with [Visual Studio Code](https://code.visualstudio.com/).


## Support the project :money_with_wings:

Are you using this project regularly and find it adding value to your life?

If yes, please consider supporting the author by donating **$5**.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/aviaryan/5)
