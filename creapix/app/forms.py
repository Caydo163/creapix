from django import forms

TYPE_CHOICES =( 
    ("black_and_white", "Noir et blanc"), 
    ("grayscale", "Echelle de gris"), 
    ("fusion", "Fusionner deux images"), 
    ("resize", "Redimensionnement"), 
    ("alignment", "Alignement vertical/horizontal"), 
    ("gif", "GIF"), 
) 

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(
        attrs={
            "class": "form-control",
            'accept': 'image/*',
        }), label="Choisir une image"
    )
    transform_type = forms.ChoiceField(choices = TYPE_CHOICES,
        widget=forms.Select(attrs={
                "class": "form-select",
        }),
        label="Choisir un type de transformation"
    )
