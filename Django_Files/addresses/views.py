import json
from django.http import HttpResponse
from .models import Addresses


# Adding/Removing Addresses Allowance Password, Should be placed within a GET parameter called E_Key

password = "pssw"


def index(req):
    instances = Addresses.objects.all()
    addresses = []
    
    for instance in instances:
        addresses.append(
            {
                "id": instance.addressId,
                "domain": instance.domainName,
                "ipv4": instance.ipv4Address,
                "port": instance.port,
            }
        )

    return HttpResponse( json.dumps(addresses) )


def add_address(req):
    if req.GET.get("E_Key") != password:
        return HttpResponse(f"Error: Incorrect Editing Key")

    required_params = ["addressId", "domainName", "ipv4Address", "port"]

    newAddress = Addresses()
    
    for param in required_params:
        if req.GET.get(param) == None:
            return HttpResponse(f"Error: Required GET Parameter {param} Was not Specified")

        setattr(newAddress, param, req.GET.get(param))

    newAddress.save()

    return HttpResponse("1")

def clear_all(req):
    if req.GET.get("E_Key") != password:
        return HttpResponse(f"Error: Incorrect Editing Key")

    Addresses.objects.all().delete()
    return HttpResponse("1")













        
