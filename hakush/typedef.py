from typing import Union, List, Dict

Json = Union[None, bool, int, float, str, List["Json"], Dict[str, "Json"]]
JsonArray = List[Json]
JsonObject = Dict[str, Json]
