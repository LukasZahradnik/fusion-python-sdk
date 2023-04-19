import asyncio
import time
from typing import Dict, Optional, Any

import httpx

from fusion import Operation


class HttpClient:
    __slots__ = "client", "headers"

    def __init__(self, client: httpx.Client, headers: Dict[str, str]):
        self.client = client
        self.headers = headers

    def await_op(self, op: Operation, timeout: float) -> Operation:
        from fjuzn.api.synchronous.operations_api import OperationsApi as SyncOperationApi

        op_api = SyncOperationApi(self)
        while True:
            op = op_api.get(op, timeout=timeout)
            if op.status == "Succeeded" or op.status == "Failed":
                return op

            time.sleep(op.retry_in / 1000)

    def post(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT
        
        headers = {**headers, **self.headers}
        response = self.client.post(url, params=params, headers=headers, json=json, timeout=timeout)
        r_json = response.json()

        op = self.await_op(Operation(**r_json), timeout)

        return op.result["resource"]

    def get(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT

        headers = {**headers, **self.headers}
        response = self.client.get(url, params=params, headers=headers, timeout=timeout, follow_redirects=True,)
        
        return response.json()

    def patch(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT

        headers = {**headers, **self.headers}
        response = self.client.patch(url, params=params, headers=headers, json=json, timeout=timeout)
        r_json = response.json()

        op = self.await_op(Operation(**r_json), timeout)

        return op.result["resource"]

    def delete(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT

        headers = {**headers, **self.headers}
        response = self.client.delete(url, params=params, headers=headers, timeout=timeout)
        r_json = response.json()

        op = self.await_op(Operation(**r_json), timeout)

        return op.result


class AsyncHttpClient:
    __slots__ = "client", "headers"

    def __init__(self, client: httpx.AsyncClient, headers: Dict[str, str]):
        self.client = client
        self.headers = headers

    async def await_op(self, op: Operation, timeout: float) -> Operation:
        from fjuzn.api.asynchronous.operations_api import OperationsApi as AsyncOperationApi

        op_api = AsyncOperationApi(self)
        while True:
            op = await op_api.get(op.id, timeout=timeout)
            if op.status == "Succeeded" or op.status == "Failed":
                return op

            await asyncio.sleep(op.retry_in / 1000)

    async def post(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT

        headers = {**headers, **self.headers}
        response = await self.client.post(url, params=params, headers=headers, json=json.to_dict(), timeout=timeout)
        r_json = response.json()

        if r_json.get("error"):
            raise Exception(r_json)

        op = await self.await_op(Operation(**r_json), timeout)

        return op.result["resource"]

    async def get(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT

        headers = {**headers, **self.headers}
        response = await self.client.get(url, params=params, headers=headers, timeout=timeout)
        r_json = response.json()

        if r_json.get("error"):
            raise Exception(r_json)

        return r_json

    async def patch(self, url: str, params, headers: Dict[str, str], json: Any, timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT

        headers = {**headers, **self.headers}
        response = await self.client.patch(url, params=params, headers=headers, json=json.to_dict(), timeout=timeout)
        r_json = response.json()

        if r_json.get("error"):
            raise Exception(r_json)

        op = await self.await_op(Operation(**r_json), timeout)

        return op.result["resource"]

    async def delete(self, url: str, params, headers: Dict[str, str], timeout: Optional[float] = None):
        if timeout is None:
            timeout = httpx.USE_CLIENT_DEFAULT

        headers = {**headers, **self.headers}
        response = await self.client.delete(url, params=params, headers=headers, timeout=timeout)
        r_json = response.json()

        if r_json.get("error"):
            raise Exception(r_json)

        op = await self.await_op(Operation(**r_json), timeout)

        return op.result
