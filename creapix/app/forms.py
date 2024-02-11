from django import forms

TYPE_CHOICES =( 
    ("black_and_white", "Noir et blanc"), 
    ("grayscale", "Echelle de gris"), 
    ("fusion", "Fusionner deux images"), 
    ("resize", "Redimensionnement"), 
    ("alignment", "Alignement vertical/horizontal"), 
    ("gif", "GIF"), 
)

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class MultipleFileField(forms.FileInput):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result

class UploadFileForm(forms.Form):
    files = forms.FileField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "accept": "image/*",
            "multiple": "true",
            "type": "File",
        }
    ), label="Choisir une ou plusieurs images")

    transform_type = forms.ChoiceField(choices = TYPE_CHOICES,
        widget=forms.Select(attrs={
                "class": "form-select",
        }),
        label="Choisir un type de transformation"
    )

    # Fusion parameters
    fusion_ratio = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "step": "0.01",
                "min": "0",
                "max": "1",
                "value": "0.5",
            }
        ),
        label="Ratio"
    )

    # Resize parameters
    resize_width = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "min": "0",
                "step": "1",
                "max": "10000",
                "value": "300",
            }
        ),
        label="Largeur"
    )
    resize_height = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "min": "0",
                "step": "1",
                "max": "10000",
                "value": "300",
            }
        ),
        label="Hauteur"
    )

    # Gif parameters
    gif_duration = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "min": "0",
                "step": "100",
                "max": "10000",
                "value": "500",
            }
        ),
        label="Durée (en ms)"
    )
