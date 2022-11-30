import typing
from typing import Iterable, Type, List, Any, NoReturn, Union, Optional, Tuple, get_origin, get_args

from typing_extensions import Annotated, TypeGuard

from orinoco.types import TypeT, AnnotationNameT


def initialize(classes: Iterable[Type[Any]]) -> List[Any]:
    return [cls_object() for cls_object in classes]


def raise_not_provided_field(field_name: str) -> NoReturn:
    raise ValueError("Field {} has to be provided".format(field_name))


def _extract_type(value: Union[TypeT, Annotated[TypeT, AnnotationNameT]]) -> Tuple[TypeT, Optional[AnnotationNameT]]:
    generic = get_origin(value)
    if generic is Annotated:
        return get_args(value)[:2]  # first two parameters - (type, annotation)
    return value, None
