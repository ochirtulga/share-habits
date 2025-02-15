from fastapi import APIRouter

habits_controller = APIRouter()


@habits_controller.get('/habits')
def get_habits():
    return {"message": "List of habits"}
