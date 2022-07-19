from odoo import api, fields, models
from odoo.osv import expression


class TaskNumber(models.Model):
    _inherit = "project.task"

    task_number = fields.Char(
        string="Task Number", requied=True, readonly=True, default="New", copy=False
    )

    @api.model
    def create(self, vals):
        if vals.get("task_number", ("New")) == ("New"):
            vals["task_number"] = self.env["ir.sequence"].next_by_code(
                "project.task"
            ) or ("New")
        return super(TaskNumber, self).create(vals)

    def name_get(self):
        task_list = []
        for task in self:
            task_list.append(
                (
                    task.id,
                    "[{}] {} - {}".format(
                        task.task_number, task.name, task.project_id.name
                    ),
                )
            )
        return task_list

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        args = args or []
        domain = []
        if name:
            domain = [
                "|",
                ("task_number", name, args, operator),
                ("name", name, args, operator),
            ]
        final_domain = expression.AND([args, domain])
        return super(TaskNumber, self).search(final_domain, limit=limit)

    def post_init_hook(self):
        """Set all task sequence number"""
        for task in self.search([]):
            task.task_number = self.env["ir.sequence"].next_by_code("project.task")
