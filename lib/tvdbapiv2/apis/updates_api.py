# coding: utf-8

"""
UpdatesApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UpdatesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def updated_query_get(self, from_time, **kwargs):
        """

        Returns an array of series that have changed in a maximum of one week blocks since the provided `fromTime`.\n\n\nThe user may specify a `toTime` to grab results for less than a week. Any timespan larger than a week will be reduced down to one week automatically.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.updated_query_get(from_time, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str from_time: Epoch time to start your date range. (required)
        :param str to_time: Epoch time to end your date range. Must be one week from `fromTime`.
        :param str accept_language: Records are returned with the Episode name and Overview in the desired language, if it exists. If there is no translation for the given language, then the record is still returned but with empty values for the translated fields.
        :return: UpdateData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['from_time', 'to_time', 'accept_language']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method updated_query_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'from_time' is set
        if ('from_time' not in params) or (params['from_time'] is None):
            raise ValueError("Missing the required parameter `from_time` when calling `updated_query_get`")

        resource_path = '/updated/query'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'from_time' in params:
            query_params['fromTime'] = params['from_time']
        if 'to_time' in params:
            query_params['toTime'] = params['to_time']

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UpdateData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def updated_query_params_get(self, **kwargs):
        """

        Returns an array of valid query keys for the `/updated/query/params` route.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.updated_query_params_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UpdateDataQueryParams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method updated_query_params_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/updated/query/params'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UpdateDataQueryParams',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
