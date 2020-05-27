from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome', db_index=True)
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'


class Exercise(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome', db_index=True)
    repetitions = models.PositiveIntegerField(verbose_name='Repetições')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'exercícios'
        verbose_name = 'exercício'


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    cpf = models.CharField(max_length=13, verbose_name='CPF')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    street = models.TextField(verbose_name='Rua')
    number = models.IntegerField(verbose_name='Número')
    district = models.TextField(verbose_name='Bairro')
    city = models.CharField(max_length=255, verbose_name='Cidade')
    application_date = models.DateField(verbose_name='Data de Matrícula')
    due_date = models.DateField(
        verbose_name='Vencimento', blank=True, null=True)
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, verbose_name='plano')
    active = models.BooleanField(blank=True, null=True)
    picture = models.ImageField(
        upload_to='student_pictures', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Estudantes"
        verbose_name = 'Estudante'


class Workout(models.Model):
    name = models.CharField(max_length=1000, null=False,
                            blank=False, help_text='Treino de perna')
    exercises = models.ManyToManyField(
        Exercise, help_text='Lista de exercicios')
    students = models.ManyToManyField(
        Student, blank=True, related_name='workout_studant')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Treinamento'
        verbose_name_plural = 'Treinamentos'


class Payment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.DO_NOTHING, verbose_name='Aluno')
    discount = models.FloatField(verbose_name='Desconto', default=0)
    value = models.PositiveIntegerField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name}, {self.created_at.date()}"

    class Meta:
        ordering = ['updated_at']
        verbose_name = 'Pagamento'
        verbose_name_plural = "Pagamentos"
