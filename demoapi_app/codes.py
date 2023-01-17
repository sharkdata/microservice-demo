#!/usr/bin/python3
# -*- coding:utf-8 -*-
# License: MIT License (see LICENSE or http://opensource.org/licenses/mit).

import logging
import fastapi
import fastapi.templating
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import demoapi_core

logger = logging.getLogger(demoapi_core.used_logger)
templates = fastapi.templating.Jinja2Templates(directory="demoapi_app/templates")
codes_router = fastapi.APIRouter()

# field
# filter
# public_value
# code
# swedish
# english
# synonyms
# ices_biology
# ices_physical_and_chemical
# bodc_nerc
# darwincore
# comments
# source


class Fields(BaseModel):
    fields: list[str]


class Values(BaseModel):
    field: str
    values: list[str]


class Translations(BaseModel):
    field: str
    value: str
    code: str
    swedish: str
    english: str


class ResponseMessage(BaseModel):
    message: str


@codes_router.get(
    "/fields/",
    tags=["Codes"],
    description="Returns a list of valid field names.",
    response_model=Fields,
    responses={404: {"model": ResponseMessage}},
)
async def get_fields(request: fastapi.Request):
    """ """
    try:
        result = demoapi_core.manager.get_fields()
        return { "fields": result }
    except Exception as e:
        logger.debug("Exception: get_fields: " + str(e))
        return JSONResponse(status_code=404, content={"message": "Fields not found"})


@codes_router.get(
    "/codes/{field}",
    tags=["Codes"],
    description="Returns a list of values for the specified field name.",
    response_model=Values,
    responses={404: {"model": ResponseMessage}},
)
async def get_values(field: str):
    """ """
    try:
        result = demoapi_core.manager.get_values_by_field(field)
        return { "field": field, "values": result}
    except Exception as e:
        logger.debug("Exception: get_values: " + str(e))
        return JSONResponse(
            status_code=404, content={"message": "Values not found"}
        )


@codes_router.get(
    "/codes/{field}/{value}",
    tags=["Codes"],
    description="Get all available translations.",
    response_model=Translations,
    responses={404: {"model": ResponseMessage}},
)
async def get_translations(field: str, value: str):
    """ """
    try:
        result = demoapi_core.manager.get_rows_by_key(field, value)
        return {
            "field": field,
            "value": value,
            "code": result.get("code", ""),
            "swedish": result.get("swedish", ""),
            "english": result.get("english", ""),
        }
    except Exception as e:
        logger.debug("Exception: get_translations: " + str(e))
        return JSONResponse(status_code=404, content={"message": "Translations not found"})
