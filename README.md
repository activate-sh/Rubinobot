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
<<<<<<< HEAD
pip install rubinobot
=======
pip install rubinobot -U
>>>>>>> origin/main
```
