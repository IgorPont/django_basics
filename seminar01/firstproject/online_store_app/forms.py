from online_store_app.models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        # Название модели, на основе которой создается форма
        model = Product
        # Включаем все поля из модели в форму
        fields = '__all__'
