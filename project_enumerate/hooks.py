from odoo import SUPERUSER_ID, api


def task_number_post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["project.task"].post_init_hook()
