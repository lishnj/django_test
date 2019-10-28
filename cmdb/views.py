from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

user_list = list()

def hello(request):
    data_dict = {"name":"老男孩", "age":25}
    data_list = ['老男孩', '51reboot']
    """
    第一种方法
    return HttpResponse("老男孩") 前端显示utf-8格式
    如果是json类型,需要添加 ensure_ascii=False 否则显示不是utf-8格式
    """
    #return HttpResponse(json.dumps(data_dict, ensure_ascii=False), content_type="application/json")

    """
    第二种方法
    如果是字典格式可以直接使用JsonResponse
    如果是列表格式，使用JsonResponse，需要添加safe=False
    使用JsonResponse都需要添加 json_dumps_params={'ensure_ascii':False} 否则显示不是UTF-8格式
    """
    #return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
    return JsonResponse(data_list, json_dumps_params={'ensure_ascii': False}, safe=False)

def index(request):
    return render(request, 'index.html')

#导入,可以使此次请求忽略csrf校验
#@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 输入的数据加到列表中
        temp = {"user": username, "pwd": password}
        user_list.append(temp)
    return render(request, "index.html", {"data": user_list})



# 计算节点权重算法
@require_POST
def nodeWeight(request):
    param = request.body  # 参数
    json_param = json.loads(param)  # 参数转json
    node = json_param["node"]
    directed = json_param["directed"]
    d = json_param["d"]
    # result = PR.main_calculate(node, directed, d)  # 调用抽象算法

    data = {"code": 200, "data": "", "message": "Success"}
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})    # 返回json格式结果
