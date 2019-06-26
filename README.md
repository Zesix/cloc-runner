# cloc-runner
A Python script that performs the following:

1. Clones a GitHub repo (only depth 1)
2. Runs [cloc](https://github.com/AlDanial/cloc) to get total lines of code
3. Deletes the cloned repo
4. Emails the output to an address specified in receiver.txt or an email address you specify.

This project is released under the [GNU General Public License 2.0](https://github.com/Zesix/cloc-runner/blob/master/LICENSE).

## Usage ##

Open receiver.txt and edit the email address to where you want the results to be sent to.

Run the script by double-clicking the script file OR open Terminal, navigate to the script location, and run:

    python3 cloc-runner.py

## Setup ##

If you are behind a corporate proxy, ensure port 443 can reach GitHub.com and port 587 can reach GMail.

Required Dependencies:

 - Git
 - Perl
 - CLOC
 - OpenSSL
 
Installation instructions for Perl, CLOC, and OpenSSL are provided below:

#### Mac OSX (Using Homebrew) ####

Open Terminal and run these commands:
1. brew install git
2. brew install cloc
3. brew install openssl

If you do not have Homebrew, use the following links to download and install the dependencies:

 - Git: http://sourceforge.net/projects/git-osx-installer/
 - Cloc: https://github.com/AlDanial/cloc#install-via-package-manager
 - OpenSSL: https://franz.com/support/openssl-mac.lhtml

#### Linux ####

Open Terminal and run these commands:
1. sudo apt install git
2. sudo apt install cloc
3. sudo apt install openssl

#### Windows ####

1. Install Git: https://gitforwindows.org/
2. Install CLOC: https://github.com/AlDanial/cloc#building-a-windows-executable
3. Install OpenSSL: https://slproweb.com/products/Win32OpenSSL.html

If you download a built binary of CLOC, add it to PATH so cloc-runner knows where to find it.
