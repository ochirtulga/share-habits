from sqlmodel import Field, SQLModel


class Habit(SQLModel, table=True):
    id: int = Field(primary_key=True)
