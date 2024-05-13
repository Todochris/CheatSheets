# Ollama
========

[Ollama](https://ollama.ai/) is a  user-friendly alternative to Llama.cpp. You download an executable that installs a service on your machine. Here is the [model library](https://ollama.com/search), once installed, you open a terminal and run:


## Installation
```bash
brew install --cask ollama # to install ollama app on mac
brew services start ollama # to have ollama server start at login
ollama run llama3 # to download and run the llama2 model
```


* [deepseek-coder](https://ollama.com/library/deepseek-coder:1.3b-instruct)
    - `ollama run deepseek-coder:1.3b-instruct` (less than 1Gb)
    - `ollama run deepseek-coder:33b-instruct` better model but slower and heavier (26Gb)
* [meta llama3]
    - `llama3:8b-instruct-q5_1` 6GB (todo replace by the bf16 GGUF model)
    - `ollama run llama3:70b-instruct-q2_K`	26 GB

## Usage

to get help on ollama commands, run:
```
ollama -h
```





# AiChat
========

[aichat](https://github.com/sigoden/aichat) Aichat: All-in-one AI-Powered CLI Chat & Copilot

to get help on commands, run:
```
aichat -h
```



