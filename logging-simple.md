# Python Simple Logging


## 1. For a Single-File Script, no UV

```python
# script.py
import logging

logging.basicConfig(
    level="DEBUG", 
    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)
log = logging.getLogger(__name__)

log.debug()
log.info()
log.warning()
log.error()
log.critical()

``` 

## 2. For Single-File Scripts, with UV

1. Create an empty Python file - `my-script.py`. 
2. Add dependency directly to this file:

```powershell
uv add --script my-script.py loguru
```

3. UV adds a comment block to `my-script.py`:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "loguru",
# ]
# ///

```

4. Import and use `logger`: 

```python
# my-script.py
from loguru import logger

logger.debug("This is a detailed debug message.")
logger.info("This script has its own built-in dependencies!")
logger.error("Something went wrong, but the formatting is beautiful.")

```

## 3. For Projects

### 2.1 main.py

```python
# main.py
import logging
import module

# Configure the root logger here, just once!
logging.basicConfig(
    level="DEBUG", 
    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    module.my_function()

```

### 2.2 module.py

```python
# module.py
import logging

# This automatically names the logger after the module (e.g., 'module')
log = logging.getLogger(__name__)

def my_function():
    log.debug("This is a debug message from the module.")
    log.info()
    log.warning()
    log.error()
    log.critical()

```
