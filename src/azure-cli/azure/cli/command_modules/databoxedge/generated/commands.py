# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ..generated._client_factory import cf_device
    databoxedge_device = CliCommandType(
        operations_tmpl='azure.mgmt.databoxedge.operations._devices_operations#DevicesOperations.{}',
        client_factory=cf_device)
    with self.command_group('databoxedge device', databoxedge_device, client_factory=cf_device,
                            min_api='2019-08-01') as g:
        g.custom_command('list', 'databoxedge_device_list')
        g.custom_show_command('show', 'databoxedge_device_show')
        g.custom_command('create', 'databoxedge_device_create', supports_no_wait=True)
        g.custom_command('update', 'databoxedge_device_update')
        g.custom_command('delete', 'databoxedge_device_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('download-update', 'databoxedge_device_download_update', supports_no_wait=True)
        g.custom_command('install-update', 'databoxedge_device_install_update', supports_no_wait=True)
        g.custom_command('scan-for-update', 'databoxedge_device_scan_for_update', supports_no_wait=True)
        g.custom_command('show-update-summary', 'databoxedge_device_show_update_summary')
        g.custom_wait_command('wait', 'databoxedge_device_show')

    from ..generated._client_factory import cf_alert
    databoxedge_alert = CliCommandType(
        operations_tmpl='azure.mgmt.databoxedge.operations._alerts_operations#AlertsOperations.{}',
        client_factory=cf_alert)
    with self.command_group('databoxedge alert', databoxedge_alert, client_factory=cf_alert,
                            min_api='2019-08-01') as g:
        g.custom_command('list', 'databoxedge_alert_list')
        g.custom_show_command('show', 'databoxedge_alert_show')

    from ..generated._client_factory import cf_bandwidth_schedule
    databoxedge_bandwidth_schedule = CliCommandType(
        operations_tmpl='azure.mgmt.databoxedge.operations._bandwidth_schedules_operations#BandwidthSchedulesOperations'
        '.{}',
        client_factory=cf_bandwidth_schedule)
    with self.command_group('databoxedge bandwidth-schedule', databoxedge_bandwidth_schedule,
                            client_factory=cf_bandwidth_schedule, min_api='2019-08-01') as g:
        g.custom_command('list', 'databoxedge_bandwidth_schedule_list')
        g.custom_show_command('show', 'databoxedge_bandwidth_schedule_show')
        g.custom_command('create', 'databoxedge_bandwidth_schedule_create', supports_no_wait=True)
        g.generic_update_command('update', custom_func_name='databoxedge_bandwidth_schedule_update',
                                 supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_bandwidth_schedule_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_bandwidth_schedule_show')

    from ..generated._client_factory import cf_job
    databoxedge_job = CliCommandType(
        operations_tmpl='azure.mgmt.databoxedge.operations._jobs_operations#JobsOperations.{}',
        client_factory=cf_job)
    with self.command_group('databoxedge', databoxedge_job, client_factory=cf_job, is_preview=True,
                            min_api='2019-08-01') as g:
        g.custom_command('show-job', 'databoxedge_show_job')

    from ..generated._client_factory import cf_node
    databoxedge_node = CliCommandType(
        operations_tmpl='azure.mgmt.databoxedge.operations._nodes_operations#NodesOperations.{}',
        client_factory=cf_node)
    with self.command_group('databoxedge', databoxedge_node, client_factory=cf_node, is_preview=True,
                            min_api='2019-08-01') as g:
        g.custom_command('list-node', 'databoxedge_list_node')

    from ..generated._client_factory import cf_order
    databoxedge_order = CliCommandType(
        operations_tmpl='azure.mgmt.databoxedge.operations._orders_operations#OrdersOperations.{}',
        client_factory=cf_order)
    with self.command_group('databoxedge order', databoxedge_order, client_factory=cf_order,
                            min_api='2019-08-01') as g:
        g.custom_command('list', 'databoxedge_order_list')
        g.custom_show_command('show', 'databoxedge_order_show')
        g.custom_command('create', 'databoxedge_order_create', supports_no_wait=True)
        g.generic_update_command('update', setter_arg_name='order', custom_func_name='databoxedge_order_update',
                                 supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_order_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_order_show')

    from ..generated._client_factory import cf_sku
    databoxedge_sku = CliCommandType(
        operations_tmpl='azure.mgmt.databoxedge.operations._skus_operations#SkusOperations.{}',
        client_factory=cf_sku)
    with self.command_group('databoxedge', databoxedge_sku, client_factory=cf_sku, is_preview=True,
                            min_api='2019-08-01') as g:
        g.custom_command('list-sku', 'databoxedge_list_sku')