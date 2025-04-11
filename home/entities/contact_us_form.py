from django import forms
from home.models import ContactUs
from home.entities.base_entity import BaseEntity


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    # method for cleaning the data
    def clean(self):
        super(ContactUsForm, self).clean()
         
        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        surname = self.cleaned_data.get('surname')
        mobile_number = self.cleaned_data.get('mobile_number')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('enquired_about')
 
        # conditions to be met for the username length
        if  not name:  # if name string is empty
            self._errors['name'] = self.error_class(['Please enter a valid name'])
        elif len(name) < 2:
            self._errors['name'] = self.error_class(['Name must have atleast 2 characters'])
        elif not name.replace(' ','').isalpha():
            self._errors['name'] = self.error_class(['Name must have alphabets only'])

        if  not email or (not BaseEntity.validate_email(email)) :
            self._errors['email'] = self.error_class(['Please enter a valid email'])

        if  not mobile_number or (not BaseEntity.validate_mobile_number(mobile_number)) :
            self._errors['mobile_number'] = self.error_class(['Please enter a valid mobile number'])

        if  surname and not surname.replace(' ','').isalpha():
            self._errors['surname'] = self.error_class(['Surname must have alphabets only'])

        
        

 
        # return any errors if found
        return self.cleaned_data


