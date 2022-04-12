from django.template import loader

from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def homeone(request):
#     return render(request,'home.html',{"name":"Jenicks","nametwo":"Elson"})

def homeone(request):
    datasample= loader.get_template('home.html')
    data={"name":"Jenicks","nametwo":"Elson",
          "Category":'Appliances',
        #   "Product":['Television','Refrigerator','Microwave oven','AC','Washing machine']  }
            "Product":[{
                'ID':1,
                'SubCategory':"Television",
                'Brand':'LG',
                'Features':['45 inch LED']
            },
            {
                'ID':2,
                'SubCategory':"Washing Machine",
                'Brand':'Samsung',
                'Features':['Fully Automatic','7 litre','Top loading']
            }
            ]}
    response=datasample.render(data,request)
    return HttpResponse(response)

def add(request):
        valone=int(request.POST["numone"])
        valtwo=int(request.POST["numtwo"])
        res = valone+valtwo
        res2 = valone * valtwo
        res3 = valone - valtwo
        return render(request,'addresult.html',{'result':res,'result2':res2,'result3':res3})



# importing from db
from .models import item

def dbitem(request):
    datasample= loader.get_template('dbitem.html')
    vals=item.objects.all()
    data={'values':vals}
    response=datasample.render(data,request)
    return HttpResponse(response)


def productdetaildisp(request,pid):
    datasample= loader.get_template('productdetails.html')
    objects=item.objects.get(id=pid)
    data={'pro':objects}
    response=datasample.render(data,request)
    return HttpResponse(response)


# def addtocart(request):
#     print(request)
#     print(request.GET['qty'])
#     print(request.GET['proid'])
#     response= HttpResponse("Item added to cart")
#     data= request.COOKIES.get('pid')
#     if data != None:
#         data=data+','+ request.GET['proid'] + ':' + request.GET['qty']
#     else:
#         data=request.GET['proid'] + ':' + request.GET['qty']
#     response.set_cookie('pid',data)
#     return response



# def viewCart(request):
#     datasample= loader.get_template('mycart.html')
#     data=request.COOKIES.get('pid')
#     if data != None:
#         items=data.split(',')
#         values=[]
#         for i in items:
#             pro=i.split(':')
#             proid= pro[0]
#             qty= pro[1]
#             values.append({proid:qty}) 
#         re={'vals':values}
#         response=datasample.render(re,request)
#     else:
#         response = datasample.render({},request)
#     return HttpResponse(response)



def addtocart(request):
    print(request)
    qty = request.GET['qty']
    proid = request.GET['proid']
    response = HttpResponse("item added to cart")
    print(request.session)
    cartitems = {}
    if (request.session.__contains__("cartdata")):
        cartitems=request.session["cartdata"]
    cartitems[proid]=qty
    request.session["cartdata"] = cartitems
    print(cartitems)    
    return response


def viewCart(request):
    page= loader.get_template('mycart.html')
    cartitems={}
    if (request.session.__contains__("cartdata")):
        for key in request.session.keys():
            item = list(request.session[key].items())
            print(item)
    return HttpResponse("cart data")






























    # response=page.render(cartitems,request)
    # return HttpResponse(response)







