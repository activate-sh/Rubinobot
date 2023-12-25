# Rubinobot
### Robinobot is a library for building self-robots in Robino based on API


## Examples

```python
from rubinobot import Client
from asyncio import run

client = Client('YOUR-AUTH')
async def main():
    results = await client.get_me()
    print(results)


run(main())
```
and
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

> [!NOTE]
> Documents will be posted soon


### contact with me
[Rubika](https://rubika.ir/activate_sh)
[Telegram](https://t.me/activate_sh)
