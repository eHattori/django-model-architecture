import requests, time
from .method_rest import Method
from .parameter_rest import Parameter
from .log_handler import Log as log


class HttpRest:

    method = Method
    parameter = Parameter

    @staticmethod
    def execute_request(url, method=None, parameter=None, retry=0):
        try:
            response = None
            start = time.time()

            if parameter is None:
                parameter = Parameter

            if method is None or method == Method.GET:
                response = requests.get(url, headers=parameter.headers, timeout=parameter.timeout)
            elif method == Method.POST:
                response = requests.post(url, json=parameter.body, headers=parameter.headers, timeout=parameter.timeout)
            elif method == Method.PUT:
                response = requests.put(url, json=parameter.body, headers=parameter.headers, timeout=parameter.timeout)
            elif method == Method.DELETE:
                response = requests.delete(url, headers=parameter.headers, timeout=parameter.timeout)

            if response.ok is False and retry <= parameter.retry:
                response = HttpRest.execute_request(url, method, parameter, retry+1)

            log.info('REQUEST: [ URL=' + url + ' STATUS_CODE=' + str(response.status_code) +
                     ' TIME=' + str((time.time() - start)) + ']')

            return response.content
        except Exception as e:
            raise e

