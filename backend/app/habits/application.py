from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from habits.controller.habits_controller import habits_controller
from habits.controller.health_check_controller import health_check_controller
from habits.constants import Constants

tags_metadata = [
    {
        "name": "health_check",
        "description": "Check the health of the application."
    },
    {
        "name": "aem_quotes",
        "description": "AEM Quotes Operations"
    },
]

app = FastAPI(root_path=Constants.CONTEXT_PATH,
              title="AEM Quotes API",
              description="AEM Quotes API",
              docs_url="/docs",
              openapi_url="/openapi.json",
              openapi_tags=tags_metadata)

origins = ["*"]  # Allow all origins for development
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(habits_controller)
app.include_router(health_check_controller)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("application:app", reload=True, host='0.0.0.0', port=80)
