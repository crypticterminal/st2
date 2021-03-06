# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc

import six

from st2auth.backends.constants import AuthBackendCapability

__all__ = [
    'BaseAuthenticationBackend'
]


@six.add_metaclass(abc.ABCMeta)
class BaseAuthenticationBackend(object):
    """
    Base authentication class.
    """

    # Capabilities offered by the auth backend
    CAPABILITIES = (
        AuthBackendCapability.CAN_AUTHENTICATE_USER
    )

    @abc.abstractmethod
    def authenticate(self, username, password):
        pass

    def get_user(self, username):
        """
        Retrieve information (user account) for a particular user.

        Note: Not all the auth backends may implement this.

        :rtype: ``dict``
        """
        raise NotImplementedError('get_user() not implemented for this backend')

    def get_user_groups(self, username):
        """
        Retrieve a list of groups a particular user is a member of.

        Note: Not all the auth backends may implement this.

        :rtype: ``list`` of ``str``
        """
        raise NotImplementedError('get_groups() not implemented for this backend')
