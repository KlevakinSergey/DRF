from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    response = Response({

        'tasks-list': reverse('tasks-list', request=request, format=format),
        'task-create': reverse('task-create', request=request, format=format),


        'tags-list': reverse('tags-list', request=request, format=format),
        'tag-create': reverse('tag-create', request=request, format=format),

    })

    return response
