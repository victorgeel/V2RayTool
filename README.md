# V2RayTool
Tool for check cloudflare worker,

get generate UUID and free V2Ray 

servers by using notebook.

# Easy to use click colab logo
[![link](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/victorgeel/facefusion-Bypass-NSFW/blob/master/FacefusionBypass.ipynb)


# Installation
+ clone
```bash
git clone https://github.com/victorgeel/V2RayTool.git
cd V2RayTool
```
+ requirements
```bash
pip install requests beautifulsoup4
```
+ make scripts executable (if you want to open with `./`)
```bash
chmod +x *.py
```

# Usage
+ **check_worker.py**
```bash
Help: python check_worker [url]

Where url looks like:
    https://example.workers.dev
```
+ **getIP.py(Cloudflare_clean_Ip)**
```bash
Help: python getIP.py [arguments]

    for only get IPs -> python getIP.py
    for save the IPs -> python getIP.py -s
    for help message -> python getIp.py [-h, --help] 
 ```
+ **getConfig.py**
```bash
Help: python getConfig.py [argumentss]

    for extracting config    -> python getConfig.py [vmess  url]
    for showing help message -> python getConfig.py [-h, --help] 
```
+ **freeV2ray.py**
```bash
Help: python freeV2ray.py [arguments]
    get free proxies -> python freeV2ray.py 20 (maximum length is 20)
    help message     -> python freeV2ray.py -h/--help 
```
