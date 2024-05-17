# Discord Bot Web Panel

![GitHub](https://img.shields.io/github/license/AdarshSudo/Discord-Bot-Web-Panel)
![GitHub issues](https://img.shields.io/github/issues/AdarshSudo/Discord-Bot-Web-Panel)
![GitHub forks](https://img.shields.io/github/forks/AdarshSudo/Discord-Bot-Web-Panel)
![GitHub stars](https://img.shields.io/github/stars/AdarshSudo/Discord-Bot-Web-Panel)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/AdarshSudo/Discord-Bot-Web-Panel)


Welcome to the Discord Bot Web Panel repository! This project aims to provide a web panel interface for managing a Discord bot.

## Setup Instructions

To set up this repository, follow these steps:

1. **Install Requirements:**
   Make sure you have Python installed (recommended version 3.11). Then, install the required packages listed in `requirements.txt`.
   Dont Forget to setup Mongodb !!

2. **Discord Developer Portal:**
   Go to the Discord Developer Portal and set up the necessary callbacks.You will find client id and client secret in Oauth2 in discord developer portal and token in bot section.
   You will need to make changes in the following files:

   - `app.py` line 110
   - `Utils.py` line 7
   - `Templates/home.html` line 70

3. **Configure Discord Bot Token:**
   Replace the placeholder token with your actual Discord bot token in the following files:

   - `config.py`
   - `utils.py` at lines 28 and 37

## Usage

Once you've completed the setup, you're ready to use the Web Panel to manage your Discord bot. Simply run the application and navigate to the provided URL to access the panel.

## Reporting Issues

If you encounter any bugs or issues while using this Web Panel, please create an issue on GitHub. Pull requests are also welcome for any improvements or fixes.

## Contact

Feel free to reach out to me on Discord if you have any questions or need assistance:
Discord Account: `adarsh_69`

**Note:** This project may contain bugs or loopholes. Your feedback and contributions are highly appreciated!


## Updates
1. ** Will be updating The Frontend and the Backend with improved UI and features in the future. **