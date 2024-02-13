from django import forms

TYPE_CHOICES =( 
    ("black_and_white", "Noir et blanc"), 
    ("grayscale", "Echelle de gris"), 
    ("fusion", "Fusionner deux images"), 
    ("resize", "Redimensionnement"), 
    ("alignment", "Alignement vertical/horizontal"), 
    ("gif", "GIF"), 
)

ALIGNMENT_DIRECTION_CHOICES = (
    ("horizontal", "Horizontale"),
    ("vertical", "Verticale"),
)

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

    # Alignment parameters
    alignment_direction = forms.ChoiceField(choices=ALIGNMENT_DIRECTION_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
        label="Choisir la direction"
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
