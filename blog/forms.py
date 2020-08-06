from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        fields = ('description',)

    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) > 256:
            raise forms.ValidationError(
                "Comment cannot exceed 256 characters.")
        return data
