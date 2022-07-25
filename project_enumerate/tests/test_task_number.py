from odoo.tests.common import TransactionCase


class TestTaskNumber(TransactionCase):
    def setUp(self):
        super(TestTaskNumber, self).setUp()
        ResPartner = self.env["res.partner"]

        # Create test partner
        self.test_partner = ResPartner.create({"name": "Test Partner"})

        # Create project
        ProjectProject = self.env["project.project"]

        self.project_1 = ProjectProject.create({"name": "Project 1"})
        self.project_2 = ProjectProject.create({"name": "Project 2"})
        self.project_3 = ProjectProject.create({"name": "Project 3"})

        # Create tasks
        TaskTask = self.env["project.task"]
        self.task_1 = TaskTask.create(
            {"name": "Test One", "project_id": self.project_1.id, "task_number": "111"}
        )

        self.task_2 = TaskTask.create(
            {"name": "Test two", "project_id": self.project_2.id, "task_number": "222"}
        )

        self.task_3 = TaskTask.create(
            {"name": "Test tree", "project_id": self.project_3.id, "task_number": "333"}
        )

    def test_name(self):
        """Test for the presence of all required fields"""
        self.assertIn("task_number", self.task_3)
        self.assertIn("name", self.task_3)
        self.assertIn("project_id", self.task_3)
        self.assertEqual(len(self.task_3.task_number), 3)

    def test_task_number(self):
        """Test task number"""
        self.assertEqual(
            self.env["project.task"].task_number,
            self.env["project.task"].id,
            msg="Task number must be equal task id",
        )

    def test_search_views(self):
        """Test search views on True"""
        test_search = self.env["project.task"].search([("task_number", "=", "111")])
        self.assertEqual(
            test_search.id, self.task_1.id, msg="Search id must be equal task id"
        )

        test_search_2 = self.env["project.task"].search([("name", "=", "Test two")])
        self.assertEqual(
            test_search_2.id, self.task_2.id, msg="Search id must be equal task id"
        )

    def test_create_new_task(self):
        """Try to create a new task"""
        ProjectProject = self.env["project.project"]

        self.project_4 = ProjectProject.create({"name": "Project 4"})
        # Creates a task...
        TaskTask = self.env["project.task"]
        self.task_4 = TaskTask.create(
            {"name": "Test four", "project_id": self.project_4.id, "task_number": "444"}
        )
        search_new = self.env["project.task"].search(
            [
                ("name", "=", "Test four"),
                ("task_number", ">", 0),
            ]
        )
        self.assertIsNot(len(search_new), 0)
        self.assertEqual(len(self.task_4.name), 9)
        self.assertEqual(
            search_new.id, self.task_4.id, msg="Search id must be equal task id"
        )
