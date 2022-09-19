# Python: Catch Warnings with Try Except

Today I needed to handle a Pillow warning. Many posts demonstrate how to treat all warnings as exceptions so they can be caught with `try` and `exept`. 

I quickly discovered that catching all warnings can be problematic. Here's how to catch specific warnings:

```
import warnings
warnings.filterwarnings("error", category=Image.DecompressionBombWarning)

def process_images():
  try:
    some_process()

  except Image.DecompressionBombWarning as e:
    print(e)
```
