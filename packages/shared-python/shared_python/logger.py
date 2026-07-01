import logging
import sys
from typing import Any, List
import structlog

def setup_logging(environment: str = "development", log_level_str: str = "INFO") -> None:
    """
    Configures structlog to output logs.
    In development, it uses ConsoleRenderer for colorized human-readable logs.
    In production, it uses JSONRenderer for ingestion into log management systems.
    """
    log_level = getattr(logging, log_level_str.upper(), logging.INFO)

    shared_processors: List[Any] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]

    if environment == "production":
        processors = shared_processors + [
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ]
    else:
        processors = shared_processors + [
            structlog.dev.ConsoleRenderer(colors=True),
        ]

    structlog.configure(
        processors=processors,
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        cache_logger_on_first_use=True,
    )

    # Configure standard library logging to route through structlog if needed
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=log_level,
    )
