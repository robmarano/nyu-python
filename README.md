# nyu-python
NYU Python Diploma Class

## Python Tutorials
* xxx

## Python Coding Style
We will be using PEP8, the standard style guide for Python Code

## Python Development Environments
For this set of courses we develop Python applications on virtual Ubuntu Linux servers
via Vagrant on your laptops using vim running via the Bash shell. Here are some links
on Vagrant:
* xxx

Here are some links to set up your environment:
* https://www.fullstackpython.com/vim.html
* https://realpython.com/vim-and-python-a-match-made-in-heaven/

### Using Vundle for setting up our vim-based Python dev env on Ubuntu
Step 1
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Step 2
touch ~/.vimrc

Step 3
Add following to ~/.vimrc file

set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)

" ...

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required


