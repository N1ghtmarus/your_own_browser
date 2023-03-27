from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    SearchNoteAPIView,
    PostNoteAPIView,
    NoteAdminViewSet,
    UpdateOrDeleteNoteAPIView,
    GetUsersNotesAPIView)
from users.views import UsersViewSet


router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet, basename='users')
router_v1.register('note_admin', NoteAdminViewSet, basename='note_admin')

urlpatterns = (
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path(
        'search_note/<str:query>/',
        SearchNoteAPIView.as_view(),
        name='search_note'
    ),
    path('create_note/', PostNoteAPIView.as_view(), name='create_note'),
    path(
        'update_note/<int:pk>/',
        UpdateOrDeleteNoteAPIView.as_view(),
        name='update_note'
    ),
    path(
        'delete_note/<int:pk>/',
        UpdateOrDeleteNoteAPIView.as_view(),
        name='delete_note'
    ),
    path(
        'get_users_notes/',
        GetUsersNotesAPIView.as_view(),
        name='get_users_notes'
    ),
)
