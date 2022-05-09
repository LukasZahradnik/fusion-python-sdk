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
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class StorageEndpoint(ResourceMetadata):
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
        'region': 'RegionRef',
        'availability_zone': 'AvailabilityZoneRef',
        'endpoint_type': 'str',
        'iscsi': 'StorageEndpointIscsi'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'region': 'region',
        'availability_zone': 'availability_zone',
        'endpoint_type': 'endpoint_type',
        'iscsi': 'iscsi'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, region=None, availability_zone=None, endpoint_type=None, iscsi=None, *args, **kwargs):  # noqa: E501
        """StorageEndpoint - a model defined in Swagger"""  # noqa: E501
        self._region = None
        self._availability_zone = None
        self._endpoint_type = None
        self._iscsi = None
        self.discriminator = None
        if region is not None:
            self.region = region
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.endpoint_type = endpoint_type
        if iscsi is not None:
            self.iscsi = iscsi
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def region(self):
        """Gets the region of this StorageEndpoint.  # noqa: E501


        :return: The region of this StorageEndpoint.  # noqa: E501
        :rtype: RegionRef
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this StorageEndpoint.


        :param region: The region of this StorageEndpoint.  # noqa: E501
        :type: RegionRef
        """

        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this StorageEndpoint.  # noqa: E501


        :return: The availability_zone of this StorageEndpoint.  # noqa: E501
        :rtype: AvailabilityZoneRef
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this StorageEndpoint.


        :param availability_zone: The availability_zone of this StorageEndpoint.  # noqa: E501
        :type: AvailabilityZoneRef
        """

        self._availability_zone = availability_zone

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this StorageEndpoint.  # noqa: E501

        The endpoint type.  # noqa: E501

        :return: The endpoint_type of this StorageEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this StorageEndpoint.

        The endpoint type.  # noqa: E501

        :param endpoint_type: The endpoint_type of this StorageEndpoint.  # noqa: E501
        :type: str
        """
        if endpoint_type is None:
            raise ValueError("Invalid value for `endpoint_type`, must not be `None`")  # noqa: E501
        allowed_values = ["iscsi"]  # noqa: E501
        if endpoint_type not in allowed_values:
            raise ValueError(
                "Invalid value for `endpoint_type` ({0}), must be one of {1}"  # noqa: E501
                .format(endpoint_type, allowed_values)
            )

        self._endpoint_type = endpoint_type

    @property
    def iscsi(self):
        """Gets the iscsi of this StorageEndpoint.  # noqa: E501


        :return: The iscsi of this StorageEndpoint.  # noqa: E501
        :rtype: StorageEndpointIscsi
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """Sets the iscsi of this StorageEndpoint.


        :param iscsi: The iscsi of this StorageEndpoint.  # noqa: E501
        :type: StorageEndpointIscsi
        """

        self._iscsi = iscsi

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
        if issubclass(StorageEndpoint, dict):
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
        if not isinstance(other, StorageEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other