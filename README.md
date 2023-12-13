# Rubino
### A library written in Python language to build the Robino robot using APIs


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
pip install rubinobot -U
```
