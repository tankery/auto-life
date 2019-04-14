# Auto Life

Auto Life is a project to try to automate any boring/repeating things in my life.

## Installation

Clone this repo and add this folder to your path, example:

``` shell
PATH_AUTO_LIFE=~/.auto-life
git clone --recurse-submodules https://github.com/tankery/auto-life $PATH_AUTO_LIFE
export PATH=$PATH:$PATH_AUTO_LIFE
# Check usability
al --help
```

## Usage

``` shell
al <action>:<target>
```


## Keep Developing

This project is just in beginning, help it grow up!

### Some Princeples

- It has a root command that can listing every other sub-commands, so I won't forget anything. (Just like Git commands)
- Argumants are optional, commands become interactive when some arguments is missing, so I won't need to remamber every argumants.
- Use Python as default language
- Private keys, access keys, certificates, should NOT included in this project, it can be listing in other private repos.

## Acknowledgements

The idea is brought from [Tyr Chen](https://github.com/tyrchen)'s WeChat article: [Code is Low](https://mp.weixin.qq.com/s/a-tUQSy5zT3qhd8mBy2HfA). Reading his writing are really a mind exploding experience.
