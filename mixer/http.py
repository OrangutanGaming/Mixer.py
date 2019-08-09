#  MIT License
#
#  Copyright (c) 2019 Nihaal Sangha (Orangutan)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import asyncio

import aiohttp

__all__ = ['HTTPv1']

class HTTPv1:
    def __init__(self, *, loop=None, base_url=None):
        """

        Parameters
        ----------
        loop : asyncio.BaseEventLoop
            The event loop to use.
        base_url : str
            The base URL. Should not have a leading slash.
        """
        loop: asyncio.BaseEventLoop = loop or asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(loop=loop)
        self.base_url = base_url or 'https://mixer.com/api/v1'

    def request(self, method, path, **kwargs):
        with self.session.request(method, f'{self.base_url}{path}', **kwargs) as r:
            pass


