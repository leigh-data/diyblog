from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)

    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) > 256:
            raise forms.ValidationError(
                "Comment cannot exceed 256 characters.")
        return data


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description',)
