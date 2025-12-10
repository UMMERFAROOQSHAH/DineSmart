from django import forms
    

class qrcodeform(forms.Form):
    restaurant_name=forms.CharField(max_length=50,label='Restauran Name',
                                    widget=forms.TextInput(attrs={
                                        'class':'form-control','placeholder':'Enter Restaurant Name','style':'border:2px solid #800080;'
                                    }))
    url=forms.URLField(max_length=200,label='Menu URL',
                        widget=forms.URLInput(attrs={
                                        'class':'form-control','placeholder':'Enter URL Of Menu','style':'border:2px solid #800080;'}))
    