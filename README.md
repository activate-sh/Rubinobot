# Rubino
### A developing library written in Python to build the Robino bot using apis


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
