[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/n4z4v0d)](https://t.me/n4z4v0d)
[![PyPI supported Python versions](https://img.shields.io/pypi/pyversions/better-automation.svg)](https://www.python.org/downloads/release/python-3116/)
[![works badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)  

Library for working with the service https://www.emailnator.com/
```python
import asyncio
from pyemailnator import CreateClient

async def main() -> str:
    client: CreateClient = CreateClient()
    random_email: str = await client.get_email()
    last_message: dict = await client.get_last_message_data(email=random_email)

    message_id: str = last_message['messageID']

    message_text: str = await client.get_message(email=random_email,
                                                 message_id=message_id)
    
    return message_text
    
if __name__ == '__main__':
    print(asyncio.run(main()))

```
# DONATE (_any evm_) - 0xDEADf12DE9A24b47Da0a43E1bA70B8972F5296F2