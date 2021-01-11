# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# Management Clients
from azure.mgmt.web import WebSiteManagementClient

# Models
from azure.mgmt.network.models import (RouteTable, Route, NetworkSecurityGroup, SecurityRule)
from azure.mgmt.web.models import AppServiceCertificatePatchResource, SiteSealRequest
from azure.mgmt.resource.resources.models import (DeploymentProperties, Deployment)

# Utils
from azure.cli.core.commands import LongRunningOperation
from azure.cli.core.commands.client_factory import (get_mgmt_service_client, get_subscription_id)
from azure.cli.core.util import (sdk_no_wait, random_string)
from knack.log import get_logger
from knack.util import CLIError
from msrestazure.tools import (parse_resource_id, is_valid_resource_id, resource_id)

logger = get_logger(__name__)


def show_appservice_certificate_order(cmd, resource_group_name, name):
    certorder_client = _get_certorder_client_factory(cmd.cli_ctx)
    return certorder_client.get(resource_group_name=resource_group_name, certificate_order_name=name)


def list_appservice_certificate_order(cmd, resource_group_name=None):
    certorder_client = _get_certorder_client_factory(cmd.cli_ctx)
    if resource_group_name:
        return certorder_client.list_by_resource_group(resource_group_name=resource_group_name)

    return certorder_client.list()


def test_appservice_certificate_order(cmd, resource_group_name, name):
    certorder_client = _get_certorder_client_factory(cmd.cli_ctx)
    kv_id = '/subscriptions/0a56b3b5-ba17-4825-9876-3706ec8fdab7/resourceGroups/certs/providers/Microsoft.KeyVault/vaults/prod-certs'
    key_vault_ref = AppServiceCertificatePatchResource(key_vault_id=kv_id, key_vault_secret_name='reddoglabs-com')
    site_seal = SiteSealRequest(light_theme=True, locale='en-us')
    return certorder_client.verify_domain_ownership(resource_group_name=resource_group_name, certificate_order_name=name)
    #return certorder_client.get_certificate(resource_group_name=resource_group_name, certificate_order_name=name, name='reddoglabs-cert')
    return certorder_client.update_certificate(resource_group_name=resource_group_name, certificate_order_name=name, name='reddoglabs-cert', key_vault_certificate=key_vault_ref)


def _get_certorder_client_factory(cli_ctx):
    client = get_mgmt_service_client(cli_ctx, WebSiteManagementClient).app_service_certificate_orders
    return client
