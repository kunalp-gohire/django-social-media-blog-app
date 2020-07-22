from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreatForm(UserCreationForm):

    class Meta:
        fields = ('username','email','first_name','last_name','password1','password2')
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address' 
        self.fields['first_name'].label= 'First Name'  
        self.fields['last_name'].label= 'Last Name'
