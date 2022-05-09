# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResourceMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'self_link': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'self_link': 'self_link',
        'display_name': 'display_name'
    }

    def __init__(self, id=None, name=None, self_link=None, display_name=None):  # noqa: E501
        """ResourceMetadata - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._self_link = None
        self._display_name = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.self_link = self_link
        if display_name is not None:
            self.display_name = display_name

    @property
    def id(self):
        """Gets the id of this ResourceMetadata.  # noqa: E501

        An immutable, globally unique, system generated identifier.  # noqa: E501

        :return: The id of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceMetadata.

        An immutable, globally unique, system generated identifier.  # noqa: E501

        :param id: The id of this ResourceMetadata.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceMetadata.  # noqa: E501

        The name of the resource, supplied by the user at creation, and used in the URI path of a resource.  # noqa: E501

        :return: The name of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceMetadata.

        The name of the resource, supplied by the user at creation, and used in the URI path of a resource.  # noqa: E501

        :param name: The name of this ResourceMetadata.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def self_link(self):
        """Gets the self_link of this ResourceMetadata.  # noqa: E501

        The URI of the resource.  # noqa: E501

        :return: The self_link of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """Sets the self_link of this ResourceMetadata.

        The URI of the resource.  # noqa: E501

        :param self_link: The self_link of this ResourceMetadata.  # noqa: E501
        :type: str
        """
        if self_link is None:
            raise ValueError("Invalid value for `self_link`, must not be `None`")  # noqa: E501

        self._self_link = self_link

    @property
    def display_name(self):
        """Gets the display_name of this ResourceMetadata.  # noqa: E501

        The display name of the resource.  # noqa: E501

        :return: The display_name of this ResourceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ResourceMetadata.

        The display name of the resource.  # noqa: E501

        :param display_name: The display_name of this ResourceMetadata.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ResourceMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other