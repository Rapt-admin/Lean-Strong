from django import forms
from home.models import User
from home.entities.base_entity import BaseEntity

class SignupForm(forms.ModelForm):
    agreement = forms.BooleanField(required=True, error_messages={'required': 'You must agree to the terms and conditions.'})

    class Meta:
        model = User
        fields = "__all__"


    # method for cleaning the data
    def clean(self):
        super(SignupForm, self).clean()
         
        # extract the username and text field from the data
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        mobile_number = self.cleaned_data.get('mobile_number')
        email = self.cleaned_data.get('email')
        agreement = self.cleaned_data.get('agreement')
 
        # conditions to be met for the username length
        if  not firstname:  # if name string is empty
            self._errors['firstname'] = self.error_class(['Please enter a valid firstname'])
        elif len(firstname) < 2:
            self._errors['firstname'] = self.error_class(['firstname must have atleast 2 characters'])
        elif not firstname.replace(' ','').isalpha():
            self._errors['firstname'] = self.error_class(['firstname must have alphabets only'])

        if  not email or (not BaseEntity.validate_email(email)) :
            self._errors['email'] = self.error_class(['Please enter a valid email'])

        if  not mobile_number or (not BaseEntity.validate_mobile_number(mobile_number)) :
            self._errors['mobile_number'] = self.error_class(['Please enter a valid mobile number'])

        if  lastname and not lastname.replace(' ','').isalpha():
            self._errors['lastname'] = self.error_class(['lastname must have alphabets only'])

        if not agreement:
            self._errors['agreement'] = self.error_class(['You must agree to the terms and conditions.'])
        
        # return any errors if found
        return self.cleaned_data
