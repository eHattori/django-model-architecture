import logging
from logging.handlers import SocketHandler
from logstash import formatter
from django.conf import settings


class TransformersFormatter(formatter.LogstashFormatterBase):
    def format(self, record):

        message = {
            '@timestamp': self.format_timestamp(record.created),
            'level': record.levelname,
            'host': self.host,
            'name': record.name,
            'msg': record.msg,
            'type': self.message_type,
            'version': settings.VERSION,
            'environment': settings.APP_ENV
        }

        message.update(self.get_extra_fields(record))

        return self.serialize(message)


class BurzumHandler(SocketHandler, object):
    def __init__(self, host, port=5959, bztoken=None, message_type='burzumlogs', tags=None, fqdn=False, version=0):
        super(BurzumHandler, self).__init__(host, port)
        self.retryFactor = 1.0
        self.retryMax = 120.0
        self.bztoken = bztoken
        self.formatter = TransformersFormatter(message_type, tags, fqdn)

    def makePickle(self, record):
        record.bztoken = self.bztoken
        return self.formatter.format(record) + b'\n'


class Logging:
    def __init__(self, message_id=None, message=None, name=None, elapsed=None, request_path=None, request_method=None,
                 request_body=None, response_status_code=None, response_body=None):
        self.version = settings.VERSION
        self.messageId = message_id
        self.message = message
        self.name = name
        self.elapsed = elapsed
        self.request = {
            'path': request_path,
            'method': request_method,
            'body': request_body,
            'response': {
                'statusCode': response_status_code,
                'body': response_body
            }
        }


class Log:

    @staticmethod
    def info(message):
        logger = logging.getLogger(__name__)
        logger.info(message)

    @staticmethod
    def error(message):
        logger = logging.getLogger(__name__)
        logger.error(message)

    @staticmethod
    def warn(message):
        logger = logging.getLogger(__name__)
        logger.warning(message)



