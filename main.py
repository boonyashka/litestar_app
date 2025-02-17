from litestar import Litestar
from litestar.static_files import create_static_files_router
import uvicorn


app = Litestar(
    route_handlers=[
        create_static_files_router(path="/static", directories=["static"]),
    ],
)

uvicorn.run("main:app", host="0.0.0.0", port=8000)
