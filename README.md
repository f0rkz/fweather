# tmux f0rkz weather (fweather)

Get the weather in your tmux status bar!

![Screenshot](screenshot.png)

# Configuration
A very minimal configuration is required to use fweather.

## API Key
An API key from [DarkSky.net / Forcast.io](https://darksky.net/) is required.

The API key needs to either be exported as `FORECASTIO_API_KEY` or loaded as a json file in:

`~/.config/fweather.json`

Which will look like this:
```json
{
      "forecastio_api_key": "YOURKEYHERE",
      "frequency": 90
}
```

Or simply plop the variable in your .bashrc .tmuxrc, etc.

```bash
export FORECASTIO_API_KEY="YOURKEYHERE"
export FWEATHER_CALL_FREQUENCY="90"
```

# Install

It is recommended to use virtualenv for fweather (or really any python project).

Once you have a virtualenv established, make sure you activate it and install the script's prerequisites.

Example:

```bash
$ source ~/venv/bin/activate
$(venv) pip install -r requirements.txt
```

Install `fweather` somewhere on your system to use with tmux:

`curl https://raw.githubusercontent.com/f0rkz/fweather/master/fweather -o ~/bin/fweather`


Enable fweather in tmux:

Example:

`set -g status-right "#(~/venv/bin/python ~/bin/fweather)"`

Reload tmux

`C-r`

# Errors
You will see a very clear message if the API key is not loaded:

![No API Key](no_api_key.png)

Other issues? I am going to try and make as many potential exceptions clear in Tmux, but there is very limited space
to work with. Its better to see what is going on with the script itself by running it by hand and reading/fixing the 
errors in the stack trace.
 
Run the script by hand and take a look at the stacktrace!

`~/bin/venv/bin/python ~/bin/fweather`
