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
    ), label="Choisir une ou plusieurs images", required=False)

    transform_type = forms.ChoiceField(choices = TYPE_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
    )

    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "type": "url",
                "aria-label": "Ajouter une image",
                "aria-describedby": "add-button",
            }
        )
    ,required=False)

    url_list = forms.CharField(widget=forms.TextInput(attrs={'hidden':'true'}), required=False)

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
    )
    fusion_x = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "min": "0",
                "step": "10",
                "max": "10000",
                "value": "0",
            }
        ),
    )
    fusion_y = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "min": "0",
                "step": "10",
                "max": "10000",
                "value": "0",
            }
        ),
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
    )

    # Alignment parameters
    alignment_direction = forms.ChoiceField(choices=ALIGNMENT_DIRECTION_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
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
    )
