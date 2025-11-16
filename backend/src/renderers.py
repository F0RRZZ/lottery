from typing import Any

from fastapi.responses import JSONResponse
import msgspec


class MsgSpecJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return msgspec.json.encode(content)
