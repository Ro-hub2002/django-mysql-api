from django.views import View
from django.utils.decorators import method_decorator
from .models import Company
from django.http import JsonResponse
from  django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': "Successfully created", 'companies': company}
            else:
                datos = {'message': "Company not Found ..."}
            return JsonResponse(datos)
            
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message': "Successfully created", 'companies': companies}
            else:
                datos = {'message': "Companies not Found ..."}
            return JsonResponse(datos)
     
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Company.objects.create(name=jd['name'],website=jd['website'], foundation=jd['foundation'])
        datos = {'message': "Successfully created"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company=Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': "Successfully created"}
        else:
            datos = {'message': "Companies not Found ..."}
        return JsonResponse(datos)


    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            datos = {'message': "Successfully deleted"}
        else:
            datos = {'message': "Companies not Found ..."}
        return JsonResponse(datos)
