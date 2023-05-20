from django.contrib import admin
from django.urls import path
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios.api.viewsets import UsuarioViewSet
from livros.api.viewsets import LivroViewSet
from emprestimos.api.viewsets import EmprestimoViewSet, EmprestimoPorUsuarioAPIView, EmprestimoEmAtraso, EmprestimoConsulta

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('livros/', LivroViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('livros/<int:pk>/', LivroViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('usuarios/', UsuarioViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('usuarios/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('emprestimos/', EmprestimoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('emprestimos/<int:pk>/', EmprestimoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('emprestimos/usuario/<int:usuario_id>/', EmprestimoPorUsuarioAPIView.as_view()),
    path('emprestimos/atraso/<int:usuario_id>/', EmprestimoEmAtraso.as_view()),
    path('emprestimos/consulta/', EmprestimoConsulta.as_view())
]