from django.urls import path
from loan_products import views


urlpatters = [
    path('loan_products/', views.home, name='loan_product_list'),
    path('loan_products/new/', views.loan_product, name='new_loan_product'),
    path('loan_products/edit/<int:id>/', views.edit, name='edit_loan_product'),
    path('loan_products/delete/<int:id>/', views.destroy, name='delete_loan_product'),
]