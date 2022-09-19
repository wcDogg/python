# Python Logging

* [logger.py](logger.py)
* [appdirs](appdirs.md)
* [Catch Specific Warnings](catch-warnings.md)


## Simple Logging

```python
import logging
logging.basicConfig(level="DEBUG", format='%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)
```

