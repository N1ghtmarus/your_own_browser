from django.db import models

from algorithms.soundex_algorithm import obj_to_soundex
from users.models import User


class Note(models.Model):
    """Модель для заметки"""
    subject = models.CharField(
        max_length=256,
        verbose_name='Тема заметки'
    )
    text = models.TextField(
        verbose_name='Текст заметки',
        blank=True
    )
    image = models.ImageField(
        upload_to='images/%Y/%m/%d',
        default=None,
        blank=True
    )
    soundex = models.TextField(
        verbose_name='soundex(subject + text в фонетическом виде)',
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Автор заметки'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    def save(self, *args, **kwargs):
        """
        Save-метод для преобразования полей subject и текст в
        фонетический вид и записи конкатенации этих полей в поле 'soundex'
        """
        self.soundex = obj_to_soundex(self.subject, self.text)
        super(Note, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-pub_date']

    def __str__(self):
        return self.subject[:79]
