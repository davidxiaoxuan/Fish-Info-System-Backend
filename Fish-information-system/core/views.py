from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from core.models import Fish  # 确保导入了Fish模型
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
import json  # 确保导入了json模块
import logging

# 配置日志记录器
logger = logging.getLogger(__name__)

def test_endpoint(request):
    data = {"message": "API is working!"}
    return JsonResponse(data)

def home(request):
    return HttpResponse("Welcome to the Fish Info System Home Page")

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)
            user = User.objects.create(
                username=email,
                email=email,
                password=make_password(password)
            )
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Received login data: {data}")  # 添加日志记录
            email = data['email']
            password = data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                return JsonResponse({'message': 'Login successful', 'user': {'id': user.id, 'email': user.email}}, status=200)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")  # 添加错误日志
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def search_fish(request):
    if request.method == "GET":
        try:
            query = request.GET.get('query', '')
            logger.info(f"Received search query: {query}")  # 添加日志记录
            if query:
                results = Fish.objects.filter(name__icontains=query)
                data = [{"id": fish.id, "name": fish.name} for fish in results]
                logger.info(f"Search results: {data}")  # 添加日志记录
                return JsonResponse(data, safe=False)
            else:
                return JsonResponse({"error": "No query provided"}, status=400)
        except Exception as e:
            logger.error(f"Error occurred during search: {str(e)}")  # 添加错误日志
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def fish_detail(request, id):
    try:
        fish = Fish.objects.get(id=id)
        data = {
            'id': fish.id,
            'name': fish.name,
            'email': fish.email,
            'age': fish.age
        }
        return JsonResponse(data)
    except Fish.DoesNotExist:
        raise Http404("Fish not found")

