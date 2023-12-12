from client import Client
from asyncio import run

client = Client('mbezkzljpbrkzaxvdwcvnyuirelpqkzy')

# 5ed8cf7a3b77500790814d80 activate_sh
async def main():
    res = await client.add_post(
        profile_id=None,
        file='wp10514840.jpg'
    )
    print(res)


if __name__ == '__main__':
    run(main())
