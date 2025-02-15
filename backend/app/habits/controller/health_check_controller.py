# Import FastAPI
from fastapi import APIRouter

# Create an instance of the FastAPI application
health_check_controller = APIRouter()


# Define a route for the health check
@health_check_controller.get("/health", tags=["health_check"])
async def health_check():
    return 'OK'
