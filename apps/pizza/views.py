from django.db.models import Q, Max, Min, Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer


class PizzaListCreateView(APIView):
    def get(self, *args, **kwargs):
        # pizzas = PizzaModel.objects.all()
        # pizzas = pizzas.filter(Q(size=30) | Q(name='Roma'))
        # pizzas = PizzaModel.objects.filter(Q(size=30) | Q(name='Roma')).exclude(price=1000).order_by('-size', '-price').reverse()
        # pizzas = PizzaModel.objects.all()[0:10:3]
        # pizzas = PizzaModel.objects.all().values('id', 'name', 'price')
        # aggregate = PizzaModel.objects.aggregate(Min('size'), Max('size'))
        # print(aggregate)
        # annotate = PizzaModel.objects.values('size').annotate(count=Count('size'))
        # print(annotate)
        # print(pizzas.query)
        # print(pizzas)
        # return Response('OK')
        # serializer = PizzaSerializer(pizzas, many=True)
        # return Response(serializer.data, status.HTTP_200_OK)
        qs = PizzaModel.objects.all()
        serializer = PizzaSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class PizzaRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response({'Details': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PizzaSerializer(pizza)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response({'Details': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = self.request.data
        serializer = PizzaSerializer(pizza, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            PizzaModel.objects.get(pk=pk).delete()
        except PizzaModel.DoesNotExist:
            return Response({'Details': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
