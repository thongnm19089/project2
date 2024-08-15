from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm, SetPasswordForm
from .models import *
from django import forms
from django.forms import ModelMultipleChoiceField
GENDER_CHOICES = (
    (True, 'Male'),
    (False, 'Female'),
)
STATUS_CHOICES = (
    (1, 'Pending'),
    (2, 'Processing'),
    (3, 'Cancel'),
    (4, 'Delivered'),
)
CITY_CHOICES = (
    ('hanoi', 'Hà Nội'),
    ('danang', 'Đà Nẵng'),
    ('hochiminh', "Hồ Chí Minh"),
    ('thanhhoa', 'Thanh Hóa'),
    ('thaibinh', "Thái Bình")
)
DISTRICT_CHOICES = (
    ('haibatrung', 'Hai Bà Trưng'),
    ('hoangmai', 'Hoàng Mai'),
    ('badinh', 'Ba Đình'),
    ('thanhxuan', 'Thanh Xuân'),
    ('hoankiem', 'Hoàn Kiếm')
)
#for register new user(customer)
class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Enter Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Confirm Password"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
#for update password
class ChangePasswordForm(SetPasswordForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Old Password'}))
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'New Password'}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Confirm New Password'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

#for edit user(customer)
class UserForm(ModelForm):
    birth = forms.DateField(widget=forms.DateInput(attrs= {'type':'date', 'class':'form-control form-inline','placeholder':'Select date of birth'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-inline', 'style': 'margin-left: 10px;'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Email Address'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    avatar = forms.ImageField(widget=forms.FileInput(),required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'birth', 'gender', 'email', 'phone', 'avatar']
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
# for add a new product
class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cat', 'price_im', 'price_sell', 'suppiler', 'description', 'is_sale', 'sale_price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Name'}),
            'cat': forms.Select(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'price_im': forms.NumberInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input','placeholder':'Import Price'}),
            'price_sell': forms.NumberInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input','placeholder':'Sell Price'}),
            'suppiler': forms.Select(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'description': forms.Textarea(attrs={'rows':5, 'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-textarea focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'is_sale': forms.CheckboxInput(attrs={'class':'text-purple-600 form-checkbox focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'sale_price': forms.NumberInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input','placeholder':'Sale Price'}),
            'image': forms.FileInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].queryset = Category.objects.all()
        self.fields['suppiler'].queryset = Suppiler.objects.all()
class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cat', 'price_im', 'price_sell', 'suppiler', 'quantity', 'description', 'is_sale', 'sale_price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Name'}),
            'cat': forms.Select(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'price_im': forms.NumberInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input','placeholder':'Import Price'}),
            'price_sell': forms.NumberInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input','placeholder':'Sell Price'}),
            'suppiler': forms.Select(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'quantity': forms.NumberInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input','placeholder':'Quantity'}),
            'description': forms.Textarea(attrs={'rows':5, 'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-textarea focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'is_sale': forms.CheckboxInput(attrs={'class':'text-purple-600 form-checkbox focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
            'sale_price': forms.NumberInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input','placeholder':'Sale Price'}),
            'image': forms.FileInput()
        }
class SuppilerForm(ModelForm):
    cat = ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-multiselect focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}))
    class Meta:
        model = Suppiler
        fields = ['name', 'phone', 'address', 'cat', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Company Name'}),
            'phone': forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Phone Number'}),
            'address': forms.Textarea(attrs={'rows':2, 'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-textarea focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray','placeholder':'Company Address'}),
            'image': forms.FileInput(),
        }
class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        widgets ={
            'name': forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Category Name'}),
            'parent': forms.Select(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
        }
class CustomerForm(ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-inline', 'style': 'margin-left: 10px;'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'birth', 'gender', 'email', 'phone', 'avatar']
        widgets = {
            'username':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Username'}),
            'first_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Last Name'}),
            'birth':forms.DateInput(attrs= {'type':'date','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Select date of Birth'}),
            'email':forms.TextInput(attrs={'type':'email','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Email address'}),
            'phone':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Phone Number'}),
            'avatar':forms.FileInput()
        }
class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['suppiler']
        widgets ={
            'suppiler': forms.Select(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray'}),
        }
class ChangeInvoiceStatus(ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class':"block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray"}))
    class Meta:
        model = Invoice
        fields = ['status']
class ChangeOrderStatus(ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class':"block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray"}))
    class Meta:
        model = Order
        fields = ['status']
class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Email',
            'onfocus': "this.placeholder = ''",
        })
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'New password',
            'onfocus': "this.placeholder = ''",
        })
        self.fields['new_password2'].widget.attrs.update({
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Confirm password',
            'onfocus': "this.placeholder = ''",
        })
class UserShippingForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Last Name"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Phone"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Address"}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Zipcode"}))
    city = forms.ChoiceField(choices=CITY_CHOICES, widget=forms.Select(attrs={'class':"country_select"}))
    district = forms.ChoiceField(choices=DISTRICT_CHOICES, widget=forms.Select(attrs={'class':"country_select"}))

    def __init__(self, user, *args, **kwargs):
        super(UserShippingForm, self).__init__(*args, **kwargs)
        shipping_address = user.shippingaddress_set.first()
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['phone'].initial = user.phone
        if shipping_address:
            self.fields['city'].initial = shipping_address.city
            self.fields['district'].initial = shipping_address.district
            self.fields['address'].initial = shipping_address.address
            self.fields['zipcode'].initial = shipping_address.zipcode
        else:
            # Khởi tạo giá trị mặc định cho các trường nếu không có địa chỉ vận chuyển được tìm thấy
            self.fields['city'].initial = ""
            self.fields['district'].initial = ""
            self.fields['address'].initial = ""
            self.fields['zipcode'].initial = ""

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']  # Sửa dòng này để lưu số điện thoại
        user.save()
        shipping_address, created = user.shippingaddress_set.get_or_create(defaults={})
        shipping_address.city = self.cleaned_data['city']
        shipping_address.district = self.cleaned_data['district']
        shipping_address.address = self.cleaned_data['address']
        shipping_address.zipcode = self.cleaned_data['zipcode']
        shipping_address.save()
class StaffForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':"Enter Password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':"Confirm Password"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-inline', 'style': 'margin-left: 10px;'}))
    class Meta:
        model = User
        fields = ['username','password1', 'password2', 'first_name', 'last_name', 'birth', 'gender', 'email', 'phone']
        widgets = {
            'username':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Username'}),
            'password1':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Password'}),
            'password2':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Confirm Password'}),
            'first_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Last Name'}),
            'birth':forms.DateInput(attrs= {'type':'date','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Select date of Birth'}),
            'email':forms.TextInput(attrs={'type':'email','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Email address'}),
            'phone':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Phone Number'}),
        }
    def save(self, commit=True):
        user = super(StaffForm, self).save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user
class UpdateStaffForm(ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-inline', 'style': 'margin-left: 10px;'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'birth', 'gender', 'email', 'phone']
        widgets = {
            'username':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Username'}),
            'first_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Last Name'}),
            'birth':forms.DateInput(attrs= {'type':'date','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Select date of Birth'}),
            'email':forms.TextInput(attrs={'type':'email','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Email address'}),
            'phone':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':'Phone Number'}),
        }
class UpdateStaffPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':"Enter Password"}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input', 'placeholder':"Confirm Password"}))
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')


        

