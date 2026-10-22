<<<<<<< HEAD
# FastAPI entry point
=======
>>>>>>> c3454979ac21ca7e12a37a19b8ef0ef4c5e82e62
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.demo import router as demo_router


def create_app() -> FastAPI:
    app = FastAPI(title="SatQuery AI", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        allow_credentials=True,
        allow_methods=["POST"],
        allow_headers=["*"],
    )
    app.include_router(demo_router)
    return app


<<<<<<< HEAD
app = create_app()
=======
app = create_app()
>>>>>>> c3454979ac21ca7e12a37a19b8ef0ef4c5e82e62
