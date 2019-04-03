from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=30, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"


class Candidate(models.Model):
    name = models.CharField(max_length=30, verbose_name="имя")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name="планета обитания")
    age = models.PositiveSmallIntegerField(verbose_name="возраст")
    email = models.EmailField(verbose_name="email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"


class Jedi(models.Model):
    name = models.CharField(max_length=30, verbose_name="имя")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name="планета, на которой он обучает")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Джедай"
        verbose_name_plural = "Джедаи"


class PadawanTest(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name="код ордена")
    padawan = models.OneToOneField(Candidate, on_delete=models.CASCADE, verbose_name="кандидат в падаваны")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Тестовое испытание падавана"
        verbose_name_plural = "Тестовое испытания падаванов"


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name="вопрос")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    answer = models.BooleanField(verbose_name="ответ")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="вопрос")
    test = models.ForeignKey(PadawanTest, on_delete=models.CASCADE, verbose_name="тестовое испытание")

    def __str__(self):
        return str(self.answer)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
