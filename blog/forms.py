"""Forms of the blog app."""
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Form for submitting the blog post."""

    class Meta:
        """Configuration of form."""

        model = Post
        fields = ('title', 'text',)
