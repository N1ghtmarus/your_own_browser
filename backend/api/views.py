from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .models import Note
from algorithms.search_algorithm import search_notes
from .pagination import CustomPagination
from .permissions import IsAdminrPermission
from .serializers import (
    SearchNoteSerializer,
    PostNoteSerializer,
    UpdateNoteSerializer,
    GetUsersNoteseSerializer,
    NoteAdminSerializer)


class SearchNoteAPIView(APIView):
    """Основной класс поиска заметок по пользовательскому запросу"""
    def get(self, *args, **kwargs) -> Response:
        userID = self.request.user.id
        query = self.kwargs['query']
        authors_notes = Note.objects.filter(author_id=userID).select_related('author')

        search_result = search_notes(query, authors_notes)
        serializer = SearchNoteSerializer(search_result, many=True)

        return Response({'Результат поиска': serializer.data})


class PostNoteAPIView(APIView):
    """Класс добавления заметки"""
    def post(self, *args, **kwargs) -> Response:
        note = self.request.data.get('note')

        # specifing the author explicitly, otherwise it
        # does not work and crash with "author required error"
        post_author = Note(author=self.request.user)

        serializer = PostNoteSerializer(post_author, data=note)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'Заметка успешно создана': serializer.data})


class UpdateOrDeleteNoteAPIView(APIView):
    """Класс изменения или удаления существующей заметки"""
    def patch(self, *args, **kwargs) -> Response:
        pk = self.kwargs['pk']
        data = self.request.data.get('note')
        userID = self.request.user.id
        note = get_object_or_404(Note.objects.select_related('author'), pk=pk)
        if note.author.id == userID:
            serializer = UpdateNoteSerializer(note, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Заметка успешно обновлена": serializer.data})
        return Response({"Предоставлены неверные данные"})

    def delete(self, *args, **kwargs) -> Response:
        pk = self.kwargs['pk']
        userID = self.request.user.id
        note = get_object_or_404(Note, pk=pk)
        if note.author.id == userID:
            note.delete()
            return Response("Заметка успешно удалена")
        return Response({"Предоставлены неверные данные"})


class GetUsersNotesAPIView(APIView):
    """Класс для получения всех заметок, которыми обладает пользователь"""
    def get(self, *args, **kwargs) -> Response:
        userID = self.request.user.id
        authors_notes = Note.objects.filter(author_id=userID).select_related('author')
        serializer = GetUsersNoteseSerializer(authors_notes, many=True)
        return Response({'Созданные Вами заметки:': serializer.data})


class NoteAdminViewSet(viewsets.ModelViewSet):
    """Вьюсет для CRUD-операций с заметками, только для администратора"""
    queryset = Note.objects.all()
    serializer_class = NoteAdminSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAdminrPermission,)
