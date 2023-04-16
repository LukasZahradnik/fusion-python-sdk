import asyncio
import time
from typing import Dict, Optional, Any

import httpx

from fjuzn.api.asynchronous.operations_api import OperationsApi as AsyncOperationApi
from fjuzn.api.synchronous.operations_api import OperationsApi as SyncOperationApi
from fusion import Operation

DEFAULT_AUTH = "accessToken", "oauth"


class HttpClient:
    __slots__ = "client",

    def __init__(self, client: httpx.Client):
        self.client = client

    def await_op(self, op: Operation, timeout: float) -> Operation:
        op_api = SyncOperationApi(self)
        while True:
            op = op_api.get(op, timeout=timeout)
            if op.status == "Succeeded" or op.status == "Failed":
                return op

            time.sleep(op.retry_in / 1000)

    def post(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = self.client.post(url, params=params, headers=headers, json=json, auth=DEFAULT_AUTH, timeout=timeout)
        r_json = response.json()

        op = self.await_op(Operation(**r_json), timeout)

        return op.result

    def get(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = self.client.get(url, params=params, headers=headers, auth=DEFAULT_AUTH, timeout=timeout)
        return response.json()

    def patch(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = self.client.patch(url, params=params, headers=headers, json=json, auth=DEFAULT_AUTH, timeout=timeout)
        r_json = response.json()

        op = self.await_op(Operation(**r_json), timeout)

        return op.result

    def delete(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = self.client.delete(url, params=params, headers=headers, auth=DEFAULT_AUTH, timeout=timeout)
        r_json = response.json()

        op = self.await_op(Operation(**r_json), timeout)

        return op.result


class AsyncHttpClient:
    __slots__ = "client",

    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def await_op(self, op: Operation, timeout: float) -> Operation:
        op_api = AsyncOperationApi(self)
        while True:
            op = await op_api.get(op, timeout=timeout)
            if op.status == "Succeeded" or op.status == "Failed":
                return op

            await asyncio.sleep(op.retry_in / 1000)

    async def post(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = await self.client.post(url, params=params, headers=headers, json=json, auth=DEFAULT_AUTH, timeout=timeout)
        r_json = await response.json()

        op = await self.await_op(Operation(**r_json), timeout)

        return op.result

    async def get(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = await self.client.get(url, params=params, headers=headers, auth=DEFAULT_AUTH, timeout=timeout)
        return await response.json()

    async def patch(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = await self.client.patch(url, params=params, headers=headers, json=json, auth=DEFAULT_AUTH, timeout=timeout)
        r_json = await response.json()

        op = await self.await_op(Operation(**r_json), timeout)

        return op.result

    async def delete(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        response = await self.client.delete(url, params=params, headers=headers, auth=DEFAULT_AUTH, timeout=timeout)
        r_json = await response.json()

        op = await self.await_op(Operation(**r_json), timeout)

        return op.result
