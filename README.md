# How to use?
1. [Download python](https://www.python.org/downloads/)
2. Run executable. Make sure option **add to path** is checked and install.
3. Edit `config.ini` file according to guide lines in below section
4. Open project folder
5. Open cmd in the same directory and run `pip install requests`
6. To run rotate script, run command `python run.py`

# Config file edit guide
```
[ROTATE]
# The script will wait this many seconds before rotating
ROTATE_INTERVAL_IN_SECONDS = 600

# All proxy api linked that you would like to be rotated
ENDPOINTS = ["https://node.oxyproxy.io/your-proxy-api-url"]
```

## To add multiple endpoints
```
ENDPOINTS = ["https://node.oxyproxy.io/your-proxy-api-url1", "https://node.oxyproxy.io/your-proxy-api-url2", "https://node.oxyproxy.io/your-proxy-api-url-etc"]
```
