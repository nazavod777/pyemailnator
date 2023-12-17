from urllib.parse import unquote

import httpx

from .validate_proxy import validate_proxy


class CreateClient:
    def __init__(self,
                 proxy: str | None = None):
        self.proxy: str | None = validate_proxy(proxy=proxy)

    async def _get(self,
                   url: str,
                   params: dict | None = None,
                   cookies: httpx.Cookies | None = None,
                   headers: dict | None = None) -> httpx.Response:
        async with httpx.AsyncClient(proxies={
            'http': self.proxy,
            'https': self.proxy
        } if self.proxy else None) as session:
            r: httpx.Response = await session.get(url=url,
                                                  params=params,
                                                  cookies=cookies,
                                                  headers=headers)
        r.raise_for_status()
        return r

    async def _post(self,
                    url: str,
                    params: dict | None = None,
                    json: dict | None = None,
                    data: dict | None = None,
                    cookies: httpx.Cookies | None = None,
                    headers: dict | None = None) -> httpx.Response:
        async with httpx.AsyncClient(proxies={
            'http': self.proxy,
            'https': self.proxy
        } if self.proxy else None) as session:
            r: httpx.Response = await session.post(url=url,
                                                   params=params,
                                                   json=json,
                                                   data=data,
                                                   cookies=cookies,
                                                   headers=headers)

        r.raise_for_status()
        return r

    async def _get_request_cookies(self) -> httpx.Cookies:
        r: httpx.Response = await self._get(url='https://www.emailnator.com/generate-email')

        r.raise_for_status()
        return r.cookies

    async def get_email(self,
                        use_plus_gmail: bool = False,
                        use_dot_gmail: bool = False,
                        use_google_mail: bool = True,
                        use_domain: bool = False):
        request_cookies: httpx.Cookies = await self._get_request_cookies()
        csrf_token: str = unquote(string=request_cookies.get('XSRF-TOKEN'))

        email_list: list = []

        if use_plus_gmail:
            email_list.append('plusGmail')

        if use_dot_gmail:
            email_list.append('dotGmail')

        if use_google_mail:
            email_list.append('googleMail')

        if use_domain:
            email_list.append('domain')

        json_data: dict = {
            'email': email_list
        }

        r: httpx.Response = await self._post(url='https://www.emailnator.com/generate-email',
                                             headers={
                                                 'x-xsrf-token': csrf_token,
                                                 'accept': 'application/json, text/plain, */*',
                                                 'accept-language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7,cy;q=0.6',
                                                 'content-type': 'application/json'
                                             },
                                             cookies=request_cookies,
                                             json=json_data)

        return r.json()['email'][0]

    async def get_last_message_data(self,
                                    email: str) -> dict:
        request_cookies: httpx.Cookies = await self._get_request_cookies()
        csrf_token: str = unquote(string=request_cookies.get('XSRF-TOKEN'))

        r: httpx.Response = await self._post(url='https://www.emailnator.com/message-list',
                                             headers={
                                                 'x-xsrf-token': csrf_token,
                                                 'accept': 'application/json, text/plain, */*',
                                                 'accept-language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7,cy;q=0.6',
                                                 'content-type': 'application/json'
                                             },
                                             cookies=request_cookies,
                                             json={
                                                 'email': email
                                             })

        return r.json()['messageData'][-1]

    async def get_message(self,
                          email: str,
                          message_id: str) -> str:
        request_cookies: httpx.Cookies = await self._get_request_cookies()
        csrf_token: str = unquote(string=request_cookies.get('XSRF-TOKEN'))

        r: httpx.Response = await self._post(url='https://www.emailnator.com/message-list',
                                             headers={
                                                 'x-xsrf-token': csrf_token,
                                                 'accept': 'application/json, text/plain, */*',
                                                 'accept-language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7,cy;q=0.6',
                                                 'content-type': 'application/json'
                                             },
                                             cookies=request_cookies,
                                             json={
                                                 'email': email,
                                                 'messageID': message_id
                                             })

        return r.text
