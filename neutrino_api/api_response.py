"""neutrino_api"""

from .api_error_code import APIErrorCode


class APIResponse:
    """
    API response payload, holds the response data along with any error details
    """

    def __init__(self, data=None, output_file_path=None, status_code=0, content_type="", error_code=0, error_message="", error_cause=None):
        """
        Immutable API response data

        Parameters
        ----------
        data : str | dict | None
            The response data for JSON based APIs
        output_file_path : str | None
            The local file path storing the output for file based APIs
        status_code : int
            The HTTP status code returned
        content_type : str
            The response content type (MIME type)
        error_code : int
            The API error code if any error has occurred
        error_message : str
            The API error message if any error has occurred
        error_cause : str | None
            For client-side errors or exceptions get the underlying cause
        """
        self.data = data
        self.file = output_file_path
        self.status_code = status_code
        self.content_type = content_type
        self.error_code = error_code
        self.error_message = error_message
        self.error_cause = error_cause

    def is_ok(self):
        """
        Was this request successul

        Returns
        -------
            bool
        """
        return self.data is not None or self.file is not None

    @staticmethod
    def of_data(status_code, content_type, data):
        """
        Create an API response for JSON data

        Parameters
        ---------
        status_code : int
            HTTP response status code
        content_type : str
            HTTP response content type
        data : str
            Response data

        Returns
        -------
        APIResponse
        """
        return APIResponse(data, None, status_code, content_type, 0, "", None)

    @staticmethod
    def of_output_file_path(status_code, content_type, output_file_path):
        """
        Create an API response for file data

        Parameters
        ----------
        status_code : int
            HTTP response status code
        content_type : str
            HTTP response content type
        output_file_path : str
            Response data

        Returns
        -------
            APIResponse
        """
        return APIResponse(None, output_file_path, status_code, content_type, 0, "", None)

    @staticmethod
    def of_error_code(status_code, content_type, error_code: int):
        """
        Create an API response for error code

        Parameters
        ----------
        status_code : int
            HTTP response status code
        content_type : str
            HTTP response content type
        error_code : int
            APIError error code

        Returns
        -------
        APIResponse
        """
        error_message = APIErrorCode().get_error_message(error_code)
        return APIResponse(None, None, status_code, content_type, error_code, error_message, None)

    @staticmethod
    def of_cause(error_code: int, error_cause: Exception):
        """
        Create an API response for error cause

        Parameters
        ----------
        error_code : int
            APIError error code
        error_cause : str
            The error that occurred
        Returns
        -------
        APIResponse
        """
        error_message = APIErrorCode().get_error_message(error_code)
        return APIResponse(None, None, 0, "", error_code, error_message, error_cause)

    @staticmethod
    def of_http_status(status_code, content_type, error_code, error_message):
        """
        Create an API response for status code

        Parameters
        ----------
        status_code : int
            HTTP response status code
        content_type : str
            HTTP response content type
        error_code : int
            NeutrinoAPI response error code
        error_message : string
            NeutrinoAPI response error message

        Returns
        -------
        APIResponse
        """
        return APIResponse(None, None, status_code, content_type, error_code, error_message, None)
