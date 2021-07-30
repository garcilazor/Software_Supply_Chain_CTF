# `mysoft\_log`
This library provides a general logging interface to connect to our
company CentralLog service.

## Basic Usage
```py
from mysoft_log import LogConnection

logger = LogConnection('https://log.mysoft.example.com')

logger.info('Log Established')

subsystem_logger = logger.with_context('mysubsystem')
subsystem_logger.crit('Oh No! Subsystem crashed!')
```

## Log Levels

- `LogLevel.CRIT` - An unrecoverable error has occurred
- `LogLevel.ERR` - A recoverable error has occurred
- `LogLevel.WARN` - Something is strange but may not be an error
- `LogLevel.INFO` - Informational notices

