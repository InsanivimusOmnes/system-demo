{
    "name": "project_task",
    "version": "14.0.1.0.0",
    "depends": ["project"],
    "author": "InsanivimusOmnes",
    "category": "Project/Project",
    "license": "LGPL-3",
    "website": "https://cetmix.com",
    # data files always loaded at installation
    "data": [
        "data/project_task_number_form.xml",
        "views/project_task_number_views.xml",
    ],
    "demo": ["data/project_demo.xml"],
    "post_init_hook": "task_number_post_init_hook",
}
