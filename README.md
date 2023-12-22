# Rubinobot
### Robinobot is a library for building self-robots in Robino based on API 


## Example
```python
from rubinobot import Client
from asyncio import run

client = Client('YOUR-AUTH')
async def main():
    results = await client.follow('followee_id')
    print(results)


run(main())
```


# Install
```bash
pip install rubinobot -U
```
