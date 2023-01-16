#!/usr/bin/python3
# -*- coding:utf-8 -*-

# License: MIT License (see LICENSE or http://opensource.org/licenses/mit).

import asyncio
import uvicorn
import logging
import demoapi_core


async def main():
    """ """
    logging_dir = "../DemoAPI-logging"
    settings_dir = "../DemoAPI-settings"

    # Demo API logger.
    demoapi_core.logger.setup_rotating_log(
        logging_dir=logging_dir,
        log_name="info_log.txt",
        debug_log_name="debug_log.txt",
    )
    logger = logging.getLogger(demoapi_core.used_logger)
    logger.info("\n\n")
    logger.info("Welcome to Demo API.")
    logger.info("====================")
    logger.info("")

    # Demo API configuration.
    demoapi_core.config.load_config(
        config_dir=settings_dir,
        config_file="demoapi_config.yaml",
        config_default_dir="",
        config_default_file="demoapi_config_default.yaml",
    )

    # Demo API core startup.
    logger.debug("Demo API - Core startup.")
    demoapi_core.manager.load_data(directory="data", file_name="translate_codes_NEW.txt")

    # App config.
    port = demoapi_core.config.get("demoapi_app.port", default="8000")
    port = int(port)
    host = demoapi_core.config.get("demoapi_app.host", default="0.0.0.0")
    log_level = demoapi_core.config.get("demoapi_app.log_level", default="info")

    logger.debug("Uvicorn startup at port: " + str(port) + ".")
    config = uvicorn.Config(
        "demoapi_app:app", loop="asyncio", host=host, port=port, log_level=log_level
    )
    server = uvicorn.Server(config)
    await server.serve()

    # Demo API core shutdown.
    logger.debug("Demo API shutdown started.")
    demoapi_core.manager.shutdown()
    logger.debug("Demo API shutdown done.")


if __name__ == "__main__":
    """ """
    asyncio.run(main())
