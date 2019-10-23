# Create file

Setup for Termux + Tasker to create a file in an S3 bucket from a quick action. Use with [this Tasker action](https://taskernet.com/shares/?user=AS35m8lGSOOQcsFqjpz4q%2BOrb3CewoKRL6PMnjlA3eVCwOuaGhUS4Wmx%2BX5s1j%2Bln3%2FTBlmB1Q%3D%3D&id=Task%3AQA%3A+Create+File#).

1. Clone in Termux
2. Copy `cp config.toml.example config.toml` and fill out the fields
3. Run `mkdir -p ~/.termux/tasker/`
4. Run `ln -s $HOME/path/to/file-mgmt-createt-file/run-create-file.sh $HOME/.termux/tasker/run-create-file.sh`
5. Bind a quick action in Tasker's settings to the imported task
6. Click the quick action!
