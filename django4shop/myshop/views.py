from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request,'main.html')

def page1Func(request):
    return render(request,'page1.html')

def page2Func(request):
    return render(request,'page2.html')

def cartFunc(request):
    name=request.POST["name"]
    price=request.POST["price"]
    #print(name,price)
    product ={'name':name, 'price':price}
    
    productList = [] #장바구니에 물건담기(상품명:가격)각각을 담는 전체 기억장소

    if "shop" in request.session:
        productList = request.session['shop']
        productList.append(product)
        request.session['shop']=productList
    else:
        productList.append(product)
        request.session['shop']=productList
    
    print('productList : ',productList)
    context={}
    context['products']=request.session['shop']
    return render(request,'cart.html',context)


def buyFunc(request): #결제처리
    if "shop" in request.session:
        productList = request.session['shop'] 
        #print(productList) #[{'name': '낙도의 노을 사진', 'price': '500000'},...
        total=0
        for p in productList:
            total+=int(p['price'])
        print('total :',total)
        request.session.clear() #session 제거
    
    return render(request,'buy.html',{'total':total})



