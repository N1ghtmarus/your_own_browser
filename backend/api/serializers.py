from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Note


User = get_user_model()


class GetUsersNoteseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения всех заметок,
    которыми обладает пользователь
    """
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        exclude = ('id', 'soundex',)


class SearchNoteSerializer(serializers.ModelSerializer):
    """Сериализатор для поиска заметок"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        exclude = ('id', 'soundex',)


class PostNoteSerializer(serializers.ModelSerializer):
    """Сериализатор для создания заметок"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        exclude = ('id', 'soundex',)

        extra_kwargs = {
            'author': {
                'required': False,
            },
        }


class UpdateNoteSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования заметок"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        exclude = ('id', 'soundex')


class NoteAdminSerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD-операций с заметками для admin пользователя"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        exclude = ('soundex',)
