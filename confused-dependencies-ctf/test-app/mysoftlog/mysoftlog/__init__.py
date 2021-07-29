from enum import Enum

class LogLevel(Enum):
    CRIT = 'critical'
    ERR = 'error'
    WARN = 'warn'
    INFO = 'info'

class LogConnection:
    # Establishes a connection to the CentralLog server hosted at log_url
    def __init__(self, log_url, context='', logger_id=None):
        self.log_url = log_url
        self.context = context
        if logger_id == None:
            self.logger_id = LogConnection.establish_conn(log_url)
            print(f'Log connection established, now logging with ID {self.logger_id}')
        else:
            self.logger_id = logger_id
    
    # Returns a logger with a given context prefix
    def with_context(self, context):
        return LogConnection(self.log_url, context=LogConnection.concat_context(self.context, context), logger_id=self.logger_id)

    def log(self, message, level, context):
        msg = {
            'message': message,
            'level': level,
            'context': LogConnection.concat_context(self.context, context)
        }
        self.send_message(msg)

    def crit(self, message, context=''):
        return self.log(message, LogLevel.CRIT, context)
    
    def err(self, message, context=''):
        return self.log(message, LogLevel.ERR, context)

    def warn(self, message, context=''):
        return self.log(message, LogLevel.WARN, context)
    
    def info(self, message, context=''):
        return self.log(message, LogLevel.INFO, context)


    def establish_conn(url):
        # Mock the request for now
        response = {
            'message': 'connection established',
            'logger_id': 'eb0861b3-ef5c-4504-9777-02349f790b85',
            'status': 200
        }

        return response['logger_id']

    def send_message(self, message_dict):
        # Mock the request for now, assume logging to the CentralLog server succeeded
        print(message_dict)

    def concat_context(base, suffix):
        if base == '':
            return suffix
        else:
            return f'{base}-{suffix}'
    
