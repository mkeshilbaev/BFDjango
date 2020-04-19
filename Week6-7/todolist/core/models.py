from django.db import models

from auth_.models import MyUser

TASK_DONE = 1
TASK_TODO = 2

TASK_STATUS = (
    ('is_done', 'DONE'),
    ('is_todo', 'TODO'),
)


class Project(models.Model):
    name = models.CharField(max_length=300)
    desc = models.TextField(max_length=500)
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    @property
    def tasks_count(self):
        return self.tasks.count()


class TaskDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_DONE)

    def done_tasks(self):
        return self.filter(status=TASK_DONE)

    def filter_by_status(self, status):
        return self.filter(status=status)


class TaskTodoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_TODO)

    def done_tasks(self):
        return self.filter(status=TASK_DONE)

    def filter_by_status(self, status):
        return self.filter(status=status)


class Task(models.Model):
    TASK_PRIORITY_LOW = 1
    TASK_PRIORITY_MEDIUM = 2
    TASK_PRIORITY_HIGH = 3

    TASK_PRIORITIES = (
        (TASK_PRIORITY_LOW, 'low'),
        (TASK_PRIORITY_MEDIUM, 'medium'),
        (TASK_PRIORITY_HIGH, 'high')
    )
    name = models.CharField(max_length=300, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=TASK_STATUS, default=TASK_TODO)
    is_deleted = models.BooleanField(default=False)
    description = models.TextField(default='')
    priority = models.PositiveIntegerField(choices=TASK_PRIORITIES, default=TASK_PRIORITY_MEDIUM)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='tasks', null=True)
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='created_tasks')


    objects = models.Manager()
    done_tasks = TaskDoneManager()
    todo_tasks = TaskTodoManager()

    class Meta:
        unique_together = ('project', 'name')
        ordering = ('name', 'status',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'my_tasks'

    def __str__(self):
        return self.name





