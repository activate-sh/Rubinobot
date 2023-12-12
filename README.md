# Rubino
### A small library for making the Robino robot 


## Example
```python
from rubino import Client
from asyncio import run

client = Client('YOUR-AUTH')
async def main():
    res = await client.follow('followee_id')
    print(res)


run(main())
```


# Install
```bash
pip install https://github.com/activate-sh/rubino/archive/refs/tags/Rubino-v1.3.zip
```
