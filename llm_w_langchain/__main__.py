import sys
from enum import Enum

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class AppNameEnum(str, Enum):
    ice_breaker = "ice_breaker"


class App(BaseModel):
    name: AppNameEnum


if __name__ == "__main__":
    app = App(name=AppNameEnum(sys.argv[1]))

    __import__(app.name.value).main()
    pass
