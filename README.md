# chatgpt-telegram-assistant
A telegram bot that allows you to chat with ChatGPT.

The package to interact with ChatGPT is from [here](https://github.com/acheong08/ChatGPT). Thanks to [Antonio Cheong](https://github.com/acheong08) for the great work!!!

# Currently working on...

- [X] : Run ChatGPT in Telegram locally
- [X] : Let multiple people join with the same
- [ ] : Write article on Medium
- [ ] : Run ChatGPT in Telegram on a server


# Installation

Create a Bot with [Botfather](https://t.me/botfather) and get the API key.

Add BOT_TOKEN to a file named .env in the root directory of the project. 

Install Telegram Bot API. You can do this by running the following command in your terminal:

    pip install pyTelegramBotAPI


Follow Installation and Configuration steps to install ChatGPT from [here](https://github.com/acheong08/ChatGPT)

Add SESSION_TOKEN to config.json and .env-file.

# Usage

run the following command in your terminal:

    python3 bot.py


## Result

![Using ChatGPT in Telegram](proof_of_work.png)


# Run on Linux Server

## Installation on Server 
Connect to Server via ssh and copy folder to server.

Check if Python is installed (otherwise install it).

    python3 --version

Get current path on server with pwd: /home/ubuntu/chatgpt-telegram

    scp -r folder username@hostname:~/path/to/folder

Install venv and create virtual environment:

    sudo apt-get install python3-venv
    mkdir myenv
    cd myenv
    python3 -m venv .

Activate virtual environment:
    
    source venv/bin/activate

Check if the environment is active:

    echo $VIRTUAL_ENV

Install requirements:

    pip install -r requirements.txt 

    > **Note** This may not work and you have to manually install the packages via `sudo apt ...`

## Run on Server

To run a script on a server in the background use `nohup`

    nohup python3 bot.py &

If you want to log the output of the script into a file add this:

    nohup python3 bot.py > output.log &
    or
    nohup python3 bot.py > output.log 2>%1 &

To stop the script, use `ps` to get the process id and `kill` to stop the process.
    
    ps -ef | grep python3 
    kill -9 <process id> 

or:
    jobs
    kill %<process id>

# Troubleshooting
## Chrome or Chromedriver Errors
The config.json file contained a **"proxy"**-field and it lead to an error I couldn't solve. I removed it and it worked. If you have the same problem, try to remove the field.

If you have some problems with selenium or chromedriver, make sure to have Chrome installed and that ChromeDriver is compatible with your Chrome version. You can check the version of Chrome with `google-chrome --version` and the version of ChromeDriver with `chromedriver --version`. They must have the same version!

You might also try to add the paths for the browser and driver into your `config.json` like this:
    
    "driver_exec_path": "./path/to/driver",
    "browser_exec_path": "./path/to/browser",

### Server Errors
- Stuck in "Browser spawned." 
Installed new chromedriver and google-chrome on Server.
/home/ubuntu/chatgpt-telegram-bot/venv/lib/python3.10/site-packages/revChatGPT/ChatGPT.py

- Chromedriver Issues on Server
Install the X Virtual Framebuffer display server
    apt install xvfb -y
Set DISPLAY environmental variable to :1
    export DISPLAY=:1
Start a Xvfb process in the background
    Xvfb $DISPLAY -screen $DISPLAY 1280x1024x16 &