from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
User = get_user_model()
class UserAdmin(BaseUserAdmin):
    form =UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email','First_Name','Last_Name','CSU_ID','CSU_Class','CSU_Position','CSU_Ministry','admin',)
    list_filter = ('admin','staff','active')
    fieldsets =(
        ('Authentication',{'fields':('email','password',)}),
        ('Personal Info',{'fields':('First_Name','Middle_Name','Last_Name')}),
        ('CSU Info',{'fields':('CSU_Ministry','CSU_Position','CSU_Class')}),
        ('Leadership Info',{'fields':('Cell_Component_Leader_Name','Cell_Leader_Name','Tissue_Leader_Name')}),
        ('Permissions',{'fields':('admin','staff','active')})
    )
    add_fieldsets =(
        ('Authentication',{'fields':('email','password1','password2')}),
        ('Personal Info',{'fields':('First_Name','Middle_Name','Last_Name')}),
        ('CSU Info',{'fields':('CSU_Ministry','CSU_Position','CSU_Class')}),
        ('Leadership Info',{'fields':('Cell_Component_Leader_Name','Cell_Leader_Name','Tissue_Leader_Name')}),
        ('Permissions',{'fields':('admin','staff','active')})
    )
    search_fields=('email','First_Name','Last_Name','CSU_ID')
    ordering = ('First_Name',)
    filter_horizontal =()
admin.site.register(User,UserAdmin)