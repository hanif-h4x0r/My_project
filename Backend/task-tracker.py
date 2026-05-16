#Fri, May 15


import json, operator, sys

from argparse import ArgumentParser
from datetime import datetime
from inspect import signature
from pathlib import Path
from typing import (
	Annotated,
	Callable,
	Literal,
	Optional,
	TypeAlias,
	TypedDict,
	Union,
	get_args,
	get_origin,
)
	
from tabulate import tabulate

supported_queries: dict[str, dict] = {}
TaskStatus: TypeAlias = Literal["done", "in-progress", "todo"]
DatabaseRow = TypedDict(
	"DatabaseRow",
	{"description": str, "status": TaskStatus, "created-at": str, "update-at": str},
)
