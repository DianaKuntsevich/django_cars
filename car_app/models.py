from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()



class Auto(models.Model):
    objects = None
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    id_car = models.CharField(verbose_name='ID авто', max_length=255)
    link = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    price_usd = models.DecimalField(verbose_name='Цена в USD', max_digits=10, decimal_places=2)
    price_byn = models.DecimalField(verbose_name='Цена в BYN', max_digits=10, decimal_places=2)
    price_eur = models.DecimalField(verbose_name='Цена в EUR', max_digits=10, decimal_places=2)
    price_rub = models.DecimalField(verbose_name='Цена в RUB', max_digits=10, decimal_places=2)
    city_location = models.CharField(verbose_name='Город', max_length=255)
    seller = models.CharField(verbose_name='Продавец', max_length=255)
    description = models.TextField(verbose_name='Описание')
    exchange = models.CharField(verbose_name='Обмен', max_length=255)
    organization = models.CharField(verbose_name='Организация', max_length=255)
    year = models.CharField(verbose_name='Год выпуска авто', max_length=255)
    brand = models.CharField(verbose_name='Бренд', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=255)
    condition = models.CharField(verbose_name='Состояние', max_length=255)
    alloy_wheels = models.BooleanField(verbose_name='Литые диски', default=False)
    abs = models.BooleanField(verbose_name='Система безопасности ABS', default=False)
    esp = models.BooleanField(verbose_name='Система безопасности ESP', default=False)
    anti_slip_system = models.BooleanField(verbose_name='Система безопасности антипробуксовочная', default=False)
    immobilizer = models.BooleanField(verbose_name='Система безопасности иммобилайзер', default=False)
    front_safebags = models.BooleanField(verbose_name='Подушки передние', default=False)
    side_safebags = models.BooleanField(verbose_name='Подушки боковые', default=False)
    rear_safebags = models.BooleanField(verbose_name='Подушки задние', default=False)
    rain_detector = models.BooleanField(verbose_name='Датчик дождя', default=False)
    rear_view_camera = models.BooleanField(verbose_name='Камера заднего вида', default=False)
    parktronics = models.BooleanField(verbose_name='Парктроники', default=False)
    hatch = models.BooleanField(verbose_name='Люк', default=False)
    cruise_control = models.BooleanField(verbose_name='Круиз-контроль', default=False)
    steering_wheel_media_control = models.BooleanField(verbose_name='Управление мультимедиа с руля', default=False)
    electro_seat_adjustment = models.BooleanField(verbose_name='Электрорегулировка сидений', default=False)
    front_glass_lift = models.BooleanField(verbose_name='Передние электро-стеклоподъёмники', default=False)
    rear_glass_lift = models.BooleanField(verbose_name='Задние электро-стеклоподъёмники', default=False)
    seat_heating = models.BooleanField(verbose_name='Обогрев сидений', default=False)
    mirror_heating = models.BooleanField(verbose_name='Обогрев зеркал', default=False)
    steering_wheel_heating = models.BooleanField(verbose_name='Обогрев руля', default=False)
    climate_control = models.BooleanField(verbose_name='Климат-контроль', default=False)
    aux_ipod = models.BooleanField(verbose_name='AUX или iPod', default=False)
    bluetooth = models.BooleanField(verbose_name='Bluetooth', default=False)
    cd_mp3_player = models.BooleanField(verbose_name='CD или MP3', default=False)
    usb = models.BooleanField(verbose_name='USB', default=False)
    media_screen = models.BooleanField(verbose_name='Мультимедийный экран', default=False)
    xenon_lights = models.BooleanField(verbose_name='Ксеноновые фары', default=False)
    fog_lights = models.BooleanField(verbose_name='Противотуманные фары', default=False)
    led_lights = models.BooleanField(verbose_name='Светодиодные фары', default=False)
    generation = models.CharField(verbose_name='Поколение', max_length=255)
    number_of_seats = models.CharField(verbose_name='Количество мест', max_length=255)
    engine_capacity = models.CharField(verbose_name='Мощность двигателя', max_length=255)
    engine_type = models.CharField(verbose_name='Тип двигателя', max_length=255)
    transmission_type = models.CharField(verbose_name='Тип передачи', max_length=255)
    generation_with_years = models.CharField(verbose_name='Поколение и год авто', max_length=255)
    interior_color = models.CharField(verbose_name='Цвет интерьера', max_length=255)
    interior_material = models.CharField(verbose_name='Материал интерьера', max_length=255)
    body_type = models.CharField(verbose_name='Тип автомобиля', max_length=255)
    drive_type = models.CharField(verbose_name='Тип трансмиссии', max_length=255)
    color = models.CharField(verbose_name='Цвет авто', max_length=255)
    mileage_km = models.CharField(verbose_name='Километраж ', max_length=255)

    # time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    # time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    # status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус поста', max_length=10)
    # category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='articles', verbose_name='Категория')
    # fixed = models.BooleanField(verbose_name='Зафиксировано', default=False)
    # thumbnail = models.ImageField(
    #     verbose_name='Превью объявления',
    #     blank=True,
    #     upload_to='images/thumbnails/%Y/%m/%d/',
    #     validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    # )

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        # ordering = ['-fixed',
        #             '-time_create']  # сортировка, ставим -created_at, чтобы выводились статьи в обратном порядке (сначала новые, потом старые)
        # indexes = [models.Index(
        #     fields=['-fixed', '-time_create', 'status'])]  # индексирование полей, чтобы ускорить результаты сортировки.

    def __str__(self):
        return f'{self.brand} | {self.model}'

    def get_absolute_url(self):
        return reverse('cars_detail', kwargs={'pk': self.id})




class Image(models.Model):
    image = models.URLField(max_length=255, unique=True, verbose_name='Изображение')
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='images', verbose_name='Автомобиль')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image


class Category(MPTTModel):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='URL категории', blank=True)
    description = models.TextField(verbose_name='Описание категории', max_length=300)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'app_categories'

    def __str__(self):
        return self.title
