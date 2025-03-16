from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from users.models import UserModel
from rest_framework import status

from users.serializers import UserSerializer


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        users = UserModel.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        # response = [model_to_dict(user) for user in users]
        # return Response(response, status.HTTP_200_OK)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        # user = UserModel(name=data['name'], age=data['age'], status=data['status'], weight=data['weight'])
        # user.save()
        serializer = UserSerializer(data=data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user = UserModel.objects.create(**data)
        # user = UserModel.objects.create(**serializer.data)
        # response = {'name':user.name, 'age':user.age, 'status':user.status, 'weight':user.weight}
        # response = model_to_dict(user)
        # return Response(response, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response(f'User {pk} does not exist.')
        serializer = UserSerializer(user)
        # return Response(model_to_dict(user), status.HTTP_200_OK)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response(f'User {pk} does not exist.')
        data = self.request.data
        # for k, v in data.items():
        #     setattr(user, k, v)
        # user.save()
        serializer = UserSerializer(instance=user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response(model_to_dict(user), status.HTTP_200_OK)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            UserModel.objects.get(pk=pk).delete()
        except UserModel.DoesNotExist:
            return Response(f'User {pk} does not exist.')
        return Response(status=status.HTTP_204_NO_CONTENT)
