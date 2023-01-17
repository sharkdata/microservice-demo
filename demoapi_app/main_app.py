#!/usr/bin/python3
# -*- coding:utf-8 -*-
# License: MIT License (see LICENSE or http://opensource.org/licenses/mit).

import time
import datetime
import asyncio
import logging
import fastapi
import fastapi.staticfiles
import fastapi.templating
from pydantic import BaseModel
from typing import Optional

# Demo API.
import demoapi_core
import demoapi_app

logger = logging.getLogger(demoapi_core.used_logger)

app = fastapi.FastAPI(
    title="Demo API for micro services - Codes",
    description="This is a template application for micro services."
    + "\n\nThe example service used to handle translations of coded values is "
    + "implemented in a separate python module 'codes.py', and is then included "
    + "in the main app as 'codes_router'."
    + "\n\nThis demo application also includes a YAML based configuration file, "
    + "and round logging files are used for info and debug logging. "
    + "\n\nAsyncio is used to run the python code in async mode.",
    version=demoapi_core.__version__,
)

# Include modules.
app.include_router(demoapi_app.codes_router)

app.mount(
    "/static",
    fastapi.staticfiles.StaticFiles(directory="demoapi_app/static"),
    name="static",
)
templates = fastapi.templating.Jinja2Templates(directory="demoapi_app/templates")


@app.on_event("startup")
async def startup_event():
    """ """
    logger.debug("API called: startup.")


@app.on_event("shutdown")
async def shutdown_event():
    """ """
    logger.debug("API called: shutdown.")


@app.get(
    "/",
    # tags=["Main app"],
    description="Main web page. "
    + "Not needed for an API service,  "
    + "but used as an example of a Jinja2/Template generated web page.",
    responses={
        200: {
            "content": {"text/html": {}},
            "description": "Returns an html page.",
        }
    },

)
async def web_page(request: fastapi.Request):
    """ """
    try:
        logger.debug("API called: webpage.")
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "demoapi_version": demoapi_core.__version__,
            },
            media_type="text/html",
        )
    except Exception as e:
        logger.debug("Exception: webpage: " + str(e))
