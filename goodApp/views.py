from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
import json
from goodApp.models import Parent, Enfant


# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nomComplet = data.get('nomComplet')
        cnie = data.get('cnie')
        etatFamilial = data.get('etatFamilial')
        tailleMenage = data.get('tailleMenage')
        habitat = data.get('habitat')
        adresse = data.get('adresse')
        tel = data.get('tel')
        enfants = data.get('enfants')

        parent = Parent(nomComplet=nomComplet, cnie=cnie, etatFamilial=etatFamilial, tailleMenage=tailleMenage,
                        habitat=habitat, adresse=adresse, tel=tel)
        parent.save()

        for enfant in enfants:
            enfant = Enfant(parent=parent, genre=enfant.get('genre'), age=enfant.get('age'),
                            etablissement=enfant.get('etablissement'), nScol=enfant.get('nScol'))
            enfant.save()
        response_data = {'message': 'Données reçues et enregistrées avec succès.'}
        return JsonResponse(response_data)
    else:
        return render(request, 'home.html')

@login_required(login_url='login')
def dashboard_page(request):
    nbr_mere = Parent.objects.count()
    nbr_enfant = Enfant.objects.count()
    # max_temp_today = Dht.objects.raw(
    #     "select dht.id,max(dht.temp) as temp,dht.hum,dht.dt,dep.name from tempHumApp_dht dht "
    #     "inner join tempHumApp_departemant dep on dep.id = dht.departemant_id "
    #     "where date(dht.dt) = date('now')"
    # )[0]
    # max_hum_today = Dht.objects.raw(
    #     "select dht.id,dht.temp as temp,max(dht.hum) as hum,dht.dt,dep.name from tempHumApp_dht dht "
    #     "inner join tempHumApp_departemant dep on dep.id = dht.departemant_id "
    #     "where date(dht.dt) = date('now')")[0]
    # min_temp_today = Dht.objects.raw(
    #     "select dht.id,min(dht.temp) as temp,dht.hum,dht.dt,dep.name from tempHumApp_dht dht "
    #     "inner join tempHumApp_departemant dep on dep.id = dht.departemant_id "
    #     "where date(dht.dt) = date('now')")[0]
    # min_hum_today = Dht.objects.raw(
    #     "select dht.id,dht.temp as temp,min(dht.hum) as hum,dht.dt,dep.name from tempHumApp_dht dht "
    #     "inner join tempHumApp_departemant dep on dep.id = dht.departemant_id "
    #     "where date(dht.dt) = date('now')")[0]
    #
    # ensas_datas = Dht.objects.filter(departemant_id=1).values('departemant__name', 'dt', 'temp', 'hum').order_by('dt')
    return render(request, 'dashboard.html', {
        'nbr_mere': nbr_mere,
        'nbr_enfant': nbr_enfant
    })
@login_required(login_url='login')
def filtre_age_enfant_view(request):
    if request.method == 'POST':
        age_debut = request.POST.get('ageDebut')
        age_fin = request.POST.get('ageFin')
        if age_debut and age_fin:
            data_search = Enfant.objects.values('parent__nomComplet', 'parent__tel', 'genre', 'age').filter(
                age__gte=age_debut, age__lte=age_fin).order_by('age')

            return render(request, 'filtre.html', {
                'data_table': data_search,
            })
    data = Enfant.objects.values('parent__nomComplet', 'parent__tel', 'genre', 'age').order_by('age')
    return render(request, 'filtre.html', {
        'data_table': data,
    })
