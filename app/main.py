import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def create_app() -> FastAPI():
    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.get("/")
    async def hi():
        return "hi"

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app)

