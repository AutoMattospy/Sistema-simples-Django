# Importa a bibliotecas 
import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Brand, Category, Product

# Registra o modelo Brand no painel de administração com a classe BrandAdmin
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de marcas
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    # Permite a busca por nome no painel de administração
    search_fields = ['name']
    # Adiciona um filtro para visualizar marcas ativas ou inativas
    list_filter = ['is_active']

# Registra o modelo Category no painel de administração com a classe CategoryAdmin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de categorias
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    # Permite a busca por nome no painel de administração
    search_fields = ['name']
    # Adiciona um filtro para visualizar categorias ativas ou inativas
    list_filter = ['is_active']

# Registra o modelo Product no painel de administração com a classe ProductAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de produtos
    list_display = ('title', 'brand', 'category', 'price', 'is_active', 'created_at', 'updated_at')
    # Permite a busca por título no painel de administração
    search_fields = ['title']
    # Adiciona um filtro para visualizar produtos ativos ou inativos
    list_filter = ['is_active']

    # Método para exportar produtos selecionados para um arquivo CSV
    def export_to_csv(self, request, queryset):
        # Cria uma resposta HTTP com o tipo de conteúdo CSV
        response = HttpResponse(content_type='text/csv')
        # Define o cabeçalho para download do arquivo CSV
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        # Cria um escritor CSV para escrever os dados no arquivo
        writer = csv.writer(response)
        # Escreve o cabeçalho das colunas no arquivo CSV
        writer.writerow(['título', 'marca', 'categoria', 'preço', 'ativo', 'descrição', 'criado em', 'atualizado em'])
        # Itera sobre os produtos selecionados e escreve suas informações no arquivo CSV
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.category.name, product.price, product.is_active, product.description, product.created_at, product.updated_at])
        # Retorna a resposta com o arquivo CSV
        return response

    # Define a descrição da ação de exportação para CSV que aparecerá no painel de administração
    export_to_csv.short_description = 'Exportar para CSV'
    # Adiciona a ação de exportação à lista de ações disponíveis no painel de administração
    actions = [export_to_csv]