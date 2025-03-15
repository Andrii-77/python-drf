from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from users.models import UserModel


class UserListCreateView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        user = UserModel(name=data['name'], age=data['age'], status=data['status'], weight=data['weight'])
        user.save()
        # response = {'name':user.name, 'age':user.age, 'status':user.status, 'weight':user.weight}
        response = model_to_dict(user)
        return Response(response)


class UserRetrieveUpdateDestroyView(APIView):
    pass
